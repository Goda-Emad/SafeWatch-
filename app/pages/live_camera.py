# SafeWatch - app/pages/live_camera.py

import streamlit as st
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
if "last_alert_time" not in st.session_state:
    st.session_state["last_alert_time"] = 0

ALERT_COOLDOWN = 30

# ═══════════════════════════════════════
# Camera Input
# ═══════════════════════════════════════
threshold = st.session_state.get("threshold", 0.75)

col_info, col_thresh = st.columns([3, 1])
with col_info:
    st.info("📸 التقط صورة من الكاميرا وسيتم تحليلها فوراً")
with col_thresh:
    st.metric("حد التنبيه", f"{threshold:.0%}")

st.divider()

camera_image = st.camera_input("التقط صورة")

if camera_image:
    image = Image.open(camera_image)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📷 الصورة الملتقطة")
        st.image(image, width=400)

    with col2:
        st.markdown("#### 🔍 نتيجة التحليل")

        with st.spinner("جاري التحليل..."):
            pil_image = preprocess_frame(image)
            label, confidence, all_scores = predict_image(pil_image)

        is_alert = check_alert(label, confidence, threshold)

        if is_alert:
            st.error("🚨 تم اكتشاف سلوك مشبوه!")
        else:
            st.success("✅ لا يوجد سلوك مشبوه")

        st.metric("السلوك المكتشف", label.upper())
        st.metric("نسبة الثقة", f"{confidence:.2%}")

        st.divider()
        st.markdown("#### 📊 نسب كل السلوكيات")
        for lbl, score in sorted(
            all_scores.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            color = "🔴" if lbl == "fighting" else "🟢"
            st.progress(score, text=f"{color} {lbl}: {score:.2%}")

    # ═══════════════════════════════════════
    # Alert Actions
    # ═══════════════════════════════════════
    if is_alert:
        st.divider()
        st.markdown("#### 📧 إجراءات التنبيه")

        current_time    = time.time()
        cooldown_passed = (
            current_time - st.session_state["last_alert_time"]
            > ALERT_COOLDOWN
        )

        # حفظ الصورة
        timestamp       = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshots_dir = ROOT / "alerts" / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = str(screenshots_dir / f"{timestamp}_{label}.jpg")
        image.save(screenshot_path)

        col3, col4 = st.columns(2)

        with col3:
            if st.button("📧 إرسال تنبيه بالإيميل", type="primary"):
                with st.spinner("جاري الإرسال..."):
                    success = send_alert_email(
                        label=label,
                        confidence=confidence,
                        image_path=screenshot_path
                    )
                if success:
                    st.success("✅ تم إرسال التنبيه بنجاح!")
                    st.session_state["total_emails"] = (
                        st.session_state.get("total_emails", 0) + 1
                    )
                    st.session_state["last_alert_time"] = current_time
                else:
                    st.error("❌ فشل إرسال الإيميل")

        with col4:
            if st.button("📝 تسجيل الحادثة"):
                log_alert(label, confidence, screenshot_path)
                st.success("✅ تم تسجيل الحادثة")

        st.session_state["total_alerts"] = (
            st.session_state.get("total_alerts", 0) + 1
        )

    st.session_state["total_predictions"] = (
        st.session_state.get("total_predictions", 0) + 1
    )
