# ActionLens - app/pages/image_test.py
import streamlit as st
from PIL import Image
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT))
sys.path.append(str(Path(__file__).parent.parent))

from src.predict import predict_image
from src.preprocess import preprocess_image, validate_image
from src.alert import check_alert, log_alert
from src.email_sender import send_alert_email

st.set_page_config(
    page_title="ActionLens — رفع صورة",
    page_icon="🖼️",
    layout="wide"
)

from components.sidebar import render_sidebar
st.session_state["active_page"] = "image"
render_sidebar()

dark = st.session_state.get("dark_mode", True)
lang = st.session_state.get("lang", "ar")

if dark:
    PAGE_BG = "#0a0e15"; CARD_BG = "#0d1117"; CARD_BOR = "#1e2535"
    TEXT = "#c9d1e0"; SUB = "#4a5568"; MET_BG = "#111622"
    ALERT_R_BG = "#1a0808"; ALERT_G_BG = "#081a0f"
else:
    PAGE_BG = "#eef2f7"; CARD_BG = "#ffffff"; CARD_BOR = "#dce3ed"
    TEXT = "#1a2744"; SUB = "#64748b"; MET_BG = "#f8fafc"
    ALERT_R_BG = "#fff0f0"; ALERT_G_BG = "#edfaf3"

GREEN = "#63d28c"; BLUE = "#4f8ef7"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
html, body, .stApp {{ background: {PAGE_BG} !important; font-family: 'Cairo', sans-serif !important; }}
[data-testid="stMetric"] {{
    background: {MET_BG} !important; border: 1px solid {CARD_BOR} !important;
    border-radius: 12px !important; padding: 16px !important;
}}
[data-testid="stMetricLabel"] {{ color: {SUB} !important; font-size: 0.82rem !important; }}
[data-testid="stMetricValue"] {{ color: {TEXT} !important; font-weight: 700 !important; }}
hr {{ border-color: {CARD_BOR} !important; }}
[data-testid="stFileUploader"] {{
    border: 2px dashed {GREEN}66 !important; border-radius: 14px !important;
    background: {CARD_BG} !important;
}}
</style>
""", unsafe_allow_html=True)

# ── Hero ──
hero_title = "🖼️ رفع صورة" if lang == "ar" else "🖼️ Upload Image"
hero_sub   = "ارفع صورة وحلل الحركة فوراً" if lang == "ar" else "Upload an image and detect actions instantly"
st.markdown(f"""
<div style="background:linear-gradient(135deg,{CARD_BG},{MET_BG});
            border-radius:16px;padding:28px 32px;margin-bottom:24px;
            border:1px solid {CARD_BOR};border-left:4px solid {GREEN};">
    <div style="font-size:1.8rem;font-weight:800;margin-bottom:6px;color:{GREEN};">{hero_title}</div>
    <div style="color:{SUB};font-size:0.92rem;">{hero_sub}</div>
</div>
""", unsafe_allow_html=True)

# ── Upload ──
upload_lbl = "ارفع صورة" if lang == "ar" else "Upload Image"
uploaded_file = st.file_uploader(upload_lbl, type=["jpg","jpeg","png","webp"])

if uploaded_file:
    image = Image.open(uploaded_file)
    valid, msg = validate_image(image)
    if not valid:
        st.error(f"❌ {msg}")
        st.stop()

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<div style="color:{TEXT};font-weight:700;font-size:0.95rem;margin-bottom:8px;">📷 {"الصورة المرفوعة" if lang=="ar" else "Uploaded Image"}</div>', unsafe_allow_html=True)
        st.image(image, use_column_width=True)

    with col2:
        st.markdown(f'<div style="color:{TEXT};font-weight:700;font-size:0.95rem;margin-bottom:8px;">🔍 {"نتيجة التحليل" if lang=="ar" else "Analysis Result"}</div>', unsafe_allow_html=True)

        with st.spinner("جاري التحليل..." if lang=="ar" else "Analyzing..."):
            processed = preprocess_image(image)
            label, confidence, all_scores = predict_image(processed)

        threshold = st.session_state.get("threshold", 0.75)
        is_alert  = check_alert(label, confidence, threshold)

        if is_alert:
            st.markdown(f"""
            <div style="background:{ALERT_R_BG};border-radius:12px;
                        border-right:5px solid #e74c3c;padding:14px 18px;margin-bottom:14px;">
                <span style="color:#e74c3c;font-weight:700;font-size:1rem;">
                    🚨 {"تم اكتشاف سلوك مشبوه!" if lang=="ar" else "Suspicious behavior detected!"}
                </span>
            </div>""", unsafe_allow_html=True)
            audio_path = Path(__file__).parent.parent / "assets" / "alert_sound.mp3"
            if audio_path.exists():
                st.audio(str(audio_path), autoplay=True)
        else:
            st.markdown(f"""
            <div style="background:{ALERT_G_BG};border-radius:12px;
                        border-right:5px solid {GREEN};padding:14px 18px;margin-bottom:14px;">
                <span style="color:{GREEN};font-weight:700;font-size:1rem;">
                    ✅ {"لا يوجد سلوك مشبوه" if lang=="ar" else "No suspicious behavior"}
                </span>
            </div>""", unsafe_allow_html=True)

        m1, m2 = st.columns(2)
        with m1: st.metric("السلوك" if lang=="ar" else "Action", label.upper())
        with m2: st.metric("الثقة" if lang=="ar" else "Confidence", f"{confidence:.2%}")

        st.divider()
        st.markdown(f'<div style="color:{TEXT};font-weight:700;font-size:0.88rem;margin-bottom:8px;">📊 {"نسب كل السلوكيات" if lang=="ar" else "All Action Scores"}</div>', unsafe_allow_html=True)
        for lbl, score in sorted(all_scores.items(), key=lambda x: x[1], reverse=True):
            icon = "🔴" if lbl == "fighting" else "🟢"
            st.progress(score, text=f"{icon} {lbl}: {score:.2%}")

    if is_alert:
        st.divider()
        st.markdown(f'<div style="color:{TEXT};font-weight:700;font-size:0.95rem;margin-bottom:12px;">📧 {"إجراءات التنبيه" if lang=="ar" else "Alert Actions"}</div>', unsafe_allow_html=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshots_dir = ROOT / "alerts" / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = str(screenshots_dir / f"{timestamp}_{label}.jpg")
        image.save(screenshot_path)

        col3, col4 = st.columns(2)
        with col3:
            if st.button("📧 إرسال تنبيه" if lang=="ar" else "📧 Send Alert", type="primary"):
                with st.spinner("جاري الإرسال..." if lang=="ar" else "Sending..."):
                    success = send_alert_email(label=label, confidence=confidence, image_path=screenshot_path)
                if success:
                    st.success("✅ تم الإرسال!")
                    st.session_state["total_emails"] = st.session_state.get("total_emails", 0) + 1
                else:
                    st.error("❌ فشل الإرسال")
        with col4:
            if st.button("📝 تسجيل" if lang=="ar" else "📝 Log"):
                log_alert(label, confidence, screenshot_path)
                st.success("✅ تم التسجيل!")

        st.session_state["total_alerts"] = st.session_state.get("total_alerts", 0) + 1

    st.session_state["total_predictions"] = st.session_state.get("total_predictions", 0) + 1
    st.session_state["top_action"] = label
