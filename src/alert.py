# SafeWatch - src/alert.py

import csv
from datetime import datetime
from pathlib import Path

# ═══════════════════════════════════════
# Config
# ═══════════════════════════════════════
SUSPICIOUS_CLASSES = ["fighting"]
ALERT_THRESHOLD    = 0.75
LOG_PATH           = Path("alerts/alerts_log.csv")


def check_alert(
    label: str,
    confidence: float,
    threshold: float = None
) -> bool:
    """
    بتشيك إذا كانت النتيجة تستحق تنبيه
    بتاخد الـ threshold من الـ slider لو موجود
    """
    limit = threshold if threshold is not None else ALERT_THRESHOLD
    return (
        label.lower() in SUSPICIOUS_CLASSES
        and confidence >= limit
    )


def log_alert(
    label: str,
    confidence: float,
    image_path: str = None
):
    """
    بتسجل التنبيه في alerts_log.csv
    """
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    file_exists = LOG_PATH.exists()

    with open(LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "timestamp", "label", "confidence", "image_path"
        ])

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "label":      label,
            "confidence": f"{confidence:.2%}",
            "image_path": image_path or "N/A"
        })


def get_alert_message(label: str, confidence: float) -> str:
    """
    بترجع رسالة التنبيه
    """
    return (
        f"⚠️ تم اكتشاف سلوك مشبوه!\n"
        f"النوع: {label.upper()}\n"
        f"الثقة: {confidence:.2%}\n"
        f"الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
