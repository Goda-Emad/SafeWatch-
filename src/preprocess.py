# SafeWatch - src/preprocess.py

import numpy as np
from PIL import Image, ImageOps
from pathlib import Path
import io


# ═══════════════════════════════════════
# الإعدادات
# ═══════════════════════════════════════
IMAGE_SIZE = (224, 224)  # المقاس المطلوب للموديل


# ═══════════════════════════════════════
# تجهيز الصورة
# ═══════════════════════════════════════
def preprocess_image(image: Image.Image) -> Image.Image:
    """
    بتجهز الصورة للـ predict:
    - بتحولها لـ RGB
    - بتعمل resize
    - بتعمل normalize
    """
    # تحويل لـ RGB لو RGBA أو Grayscale
    img = image.convert("RGB")

    # Resize مع الحفاظ على النسبة
    img = ImageOps.fit(img, IMAGE_SIZE, Image.Resampling.LANCZOS)

    return img


def preprocess_from_bytes(image_bytes: bytes) -> Image.Image:
    """
    بتاخد bytes (من file uploader) وبترجع صورة جاهزة
    """
    img = Image.open(io.BytesIO(image_bytes))
    return preprocess_image(img)


def preprocess_from_path(image_path: str) -> Image.Image:
    """
    بتاخد مسار صورة وبترجع صورة جاهزة
    """
    img = Image.open(Path(image_path))
    return preprocess_image(img)


def preprocess_frame(frame: np.ndarray) -> Image.Image:
    """
    بتاخد frame من الكاميرا (numpy array) وبترجع صورة جاهزة
    """
    img = Image.fromarray(frame)
    return preprocess_image(img)


def validate_image(image: Image.Image) -> tuple[bool, str]:
    """
    بتتأكد إن الصورة صالحة للاستخدام

    Returns:
        (True, "")           ← صورة صح
        (False, "السبب")     ← صورة غلط
    """
    if image is None:
        return False, "الصورة فاضية"

    width, height = image.size

    if width < 50 or height < 50:
        return False, "الصورة صغيرة جداً (أقل من 50×50)"

    if width > 5000 or height > 5000:
        return False, "الصورة كبيرة جداً (أكبر من 5000×5000)"

    return True, ""
