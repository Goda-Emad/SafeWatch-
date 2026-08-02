# SafeWatch - app/pages/live_camera.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import sys
import time
from pathlib import Path
from datetime import datetime

# ═══════════════════════════════════════
# Path Setup
# ═══════════════════════════════════════
ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT))

from src.predict import predict_image
from src.preprocess import preprocess_frame, validate_image
from src.alert import check_alert, log_alert, get_alert_message
from src.email_sender import send_alert_email

# ═══════════════════════════════════════
# Page Config
# ═══════════════════════════════════════
st.set_page_config(
    page_title="SafeWatch — كاميرا مباشرة",
    page_icon="📹",
    layout="wide"
)

st.title("📹 كاميرا مباشرة")
st.caption("مراقبة السلوك في الوقت الفعلي")
st.divider()

# ═══════════════════════════════════════
# Session State
# ═══════════════════════════════════════
if "camera_running" not in st.session_state:
    st.session_state["camera_running"] = False

if "last_alert_time" not in st.session_state:
    st.session_state["last_alert_time"] = 0

if "frame_count" not in st.session_state:
    st.session_state["frame_count"] = 0

# ═══════════════════════════════════════
# Settings
# ═══════════════════════════════════════
ALERT_COOLDOWN = 30   # ثانية بين كل تنبيه وتاني
PREDICT_EVERY  = 10   # بيعمل predict كل 10 frames

# ═══════════════════════════════════════
# Controls
# ═══════════════════════════════════════
col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)

with col_ctrl1:
    start_btn = st.button(
        "▶️ تشغيل الكاميرا",
        type="primary",
        disabled=st.session_state["camera_running"]
    )

with col_ctrl2:
    stop_btn = st.button(
        "⏹️ إيقاف الكاميرا",
        disabled=not st.session_state["camera_running"]
    )

with col_ctrl3:
    threshold = st.session_state.get("threshold", 0.75)
    st.metric("حد التنبيه", f"{threshold:.0%}")

if start_btn:
    st.session_state["camera_running"] = True

if stop_btn:
    st.session_state["camera_running"] = False

st.divider()

# ═══════════════════════════════════════
# Camera Feed
# ═══════════════════════════════════════
if st.session_state["camera_running"]:

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("#### 📷 البث المباشر")
        frame_placeholder  = st.empty()
        status_placeholder = st.empty()

    with col2:
        st.markdown("#### 📊 التحليل")
        result_placeholder = st.empty()
        scores_placeholder = st.empty()
        st.divider()
        st.markdown("#### 🚨 التنبيهات")
        alert_placeholder  = st.empty()

    # ── فتح الكاميرا ──
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("❌ مش قادر يفتح الكاميرا — تأكد إنها متوصلة")
        st.session_state["camera_running"] = False
        st.stop()

    try:
        while st.session_state["camera_running"]:
            ret, frame = cap.read()

            if not ret:
                st.error("❌ مشكلة في قراءة الكاميرا")
                break

            st.session_state["frame_count"] += 1

            # ── عرض الـ Frame ──
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(
                frame_rgb,
                channels="RGB",
                use_column_width=True        # ✅ متوافق مع Streamlit 1.35
            )

            # ── Predict كل X frames ──
            if st.session_state["frame_count"] % PREDICT_EVERY == 0:

                pil_image = preprocess_frame(frame_rgb)
                label, confidence, all_scores = predict_image(pil_image)

                # عرض النتيجة
                result_placeholder.metric(
                    label="السلوك المكتشف",
                    value=label.upper(),
                    delta=f"{confidence:.2%}"
                )

                # عرض الـ Scores
                scores_text = "\n".join([
                    f"{k}: {v:.2%}"
                    for k, v in sorted(
                        all_scores.items(),
                        key=lambda x: x[1],
                        reverse=True
                    )[:3]
                ])
                scores_placeholder.code(scores_text)

                # ── Alert ──
                is_alert = check_alert(label, confidence, threshold)
                current_time   = time.time()
                cooldown_passed = (
                    current_time - st.session_state["last_alert_time"]
                    > ALERT_COOLDOWN
                )

                if is_alert and cooldown_passed:
                    st.session_state["last_alert_time"] = current_time

                    # عرض التنبيه
                    alert_placeholder.error(
                        f"🚨 {label.upper()} — {confidence:.2%}"
                    )

                    # حفظ الصورة
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshots_dir = ROOT / "alerts" / "screenshots"
                    screenshots_dir.mkdir(parents=True, exist_ok=True)
                    screenshot_path = str(
                        screenshots_dir / f"{timestamp}_{label}.jpg"
                    )
                    Image.fromarray(frame_rgb).save(screenshot_path)

                    # تسجيل وإرسال
                    log_alert(label, confidence, screenshot_path)
                    send_alert_email(
                        label=label,
                        confidence=confidence,
                        image_path=screenshot_path
                    )

                    # تحديث الإحصائيات
                    st.session_state["total_alerts"] = (
                        st.session_state.get("total_alerts", 0) + 1
                    )
                    st.session_state["total_emails"] = (
                        st.session_state.get("total_emails", 0) + 1
                    )

                else:
                    alert_placeholder.success("✅ لا يوجد سلوك مشبوه")

            status_placeholder.caption(
                f"Frames: {st.session_state['frame_count']}"
            )

            time.sleep(0.03)  # ~30 FPS

    finally:
        cap.release()

else:
    st.info("👆 اضغط تشغيل الكاميرا للبدء")
