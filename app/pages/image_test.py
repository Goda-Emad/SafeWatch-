# SafeWatch - app/pages/image_test.py

import streamlit as st
from PIL import Image
import sys
from pathlib import Path
from datetime import datetime

# ═══════════════════════════════════════
# Path Setup
# ═══════════════════════════════════════
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.predict import predict_image
from src.preprocess import preprocess_image, validate_image
from src.alert import check_alert, log_alert
from src.email_sender import send_alert_email

# ═══════════════════════════════════════
# Page Config
# ═══════════════════════════════════════
st.set_page_config(
    page_title="SafeWatch — اختبار صورة",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ اختبار صورة")
st.caption("ارفع صورة وحلل السلوك فيها فوراً")
st.divider()

# ═══════════════════════════════════════
# Upload
# ═══════════════════════════════════════
uploaded_file = st.file_uploader(
    "ارفع صورة",
    type=["jpg", "jpeg", "png", "webp"],
    help="الصيغ المدعومة: JPG, PNG, WEBP"
)

if uploaded_file:
    image = Image.open(uploaded_file)

    # ── Validate ──
    valid, msg = validate_image(image)
    if not valid:
        st.error(f"❌ {msg}")
        st.stop()

    # ── Layout ──
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📷 الصورة المرفوعة")
        st.image(image, width=500)

    with col2:
        st.markdown("#### 🔍 نتيجة التحليل")

        with st.spinner("جاري التحليل..."):
            processed = preprocess_image(image)
            label, confidence, all_scores = predict_image(processed)

        threshold = st.session_state.get("threshold", 0.75)
        is_alert  = check_alert(label, confidence, threshold)

        if is_alert:
            st.error("🚨 تم اكتشاف سلوك مشبوه!")
            st.metric("السلوك المكتشف", label.upper())
            st.metric("نسبة الثقة", f"{confidence:.2%}")

            audio_path = Path("app/assets/alert_sound.mp3")
            if audio_path.exists():
                st.audio(str(audio_path), autoplay=True)
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

        col3, col4 = st.columns(2)

        with col3:
            if st.button("📧 إرسال تنبيه بالإيميل", type="primary"):
                with st.spinner("جاري الإرسال..."):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_path = (
                        f"alerts/screenshots/{timestamp}_{label}.jpg"
                    )
                    Path("alerts/screenshots").mkdir(
                        parents=True, exist_ok=True
                    )
                    image.save(screenshot_path)

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
