# SafeWatch - src/predict.py

import numpy as np
from PIL import Image
from pathlib import Path
try:
    from tflite_runtime.interpreter import Interpreter
except ImportError:
    from tensorflow.lite.python.interpreter import Interpreter

# ═══════════════════════════════════════
# تحميل الموديل
# ═══════════════════════════════════════
MODEL_PATH  = Path("models/model_unquant.tflite")
LABELS_PATH = Path("models/labels.txt")


def load_model():
    interpreter = Interpreter(model_path=str(MODEL_PATH))
    interpreter.allocate_tensors()
    return interpreter


def load_labels() -> list:
    """
    بتحمل الـ labels من labels.txt
    """
    with open(LABELS_PATH, "r", encoding="utf-8") as f:
        labels = [
            line.strip().split(" ", 1)[-1]  # بيشيل الرقم في الأول
            for line in f.readlines()
            if line.strip()
        ]
    return labels


# ═══════════════════════════════════════
# الـ Inference
# ═══════════════════════════════════════
def predict_image(image: Image.Image) -> tuple[str, float, dict]:
    """
    بتاخد صورة PIL وبترجع:
    - label     : اسم الكلاس
    - confidence: نسبة الثقة
    - all_scores: كل الكلاسات مع نسبها
    """
    interpreter = load_model()
    labels      = load_labels()

    # ── تجهيز الصورة ──
    input_details  = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_shape = input_details[0]["shape"]
    height, width = input_shape[1], input_shape[2]

    img = image.convert("RGB").resize((width, height))
    img_array = np.array(img, dtype=np.float32)

    # Normalize
    img_array = (img_array / 127.5) - 1.0
    img_array = np.expand_dims(img_array, axis=0)

    # ── تشغيل الموديل ──
    interpreter.set_tensor(input_details[0]["index"], img_array)
    interpreter.invoke()

    # ── النتائج ──
    output = interpreter.get_tensor(output_details[0]["index"])[0]
    scores = {labels[i]: float(output[i]) for i in range(len(labels))}

    best_label      = max(scores, key=scores.get)
    best_confidence = scores[best_label]

    return best_label, best_confidence, scores
