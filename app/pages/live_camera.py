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

# ── Load CSS ──
def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── Sidebar ──
sys.path.append(str(Path(__file__).parent.parent))
from components.sidebar import render_sidebar
render_sidebar()

# ═══════════════════════════════════════
# Session State
# ═══════════════════════════════════════
if "last_alert_time" not in st.session_state:
    st.session_state["last_alert_time"] = 0

ALERT_COOLDOWN = 30

# ═══════════════════════════════════════
# Hero
# ═══════════════════════════════════════
st.markdown("""
    <div style='
        background: linear-gradient(135deg, #1a2744 0%, #243358 100%);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 24px;
        border-left: 5px solid #f0a500;
    '>
        <h1 style='color:#f0a500; margin:0; font-size:1.9rem; border:none;'>
            📹 كاميرا مباشرة
        </h1>
        <p style='color:#c8d4e8; margin:6px 0 0; font-size:0.95rem;'>
            التقط صورة من الكاميرا وسيتم تحليلها فوراً
        </p>
    </div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# Info + Threshold
# ═══════════════════════════════════════
threshold = st.session_state.get("threshold", 0.75)

col_info, col_thresh = st.columns([3, 1])
with col_info:
    st.markdown("""
        <div style='
            background: #eaf1fb;
            border-radius: 12px;
            border-right: 4px solid #1a2744;
            padding: 14px 18px;
            color: #1a2744;
            font-weight: 600;
            font-size: 0.95rem;
        '>
            📸 التقط صورة من الكاميرا وسيتم تحليلها فوراً
        </div>
    """, unsafe_allow_html=True)
with col_thresh:
    st.metric("حد التنبيه", f"{threshold:.0%}")

st.divider()

# ═══════════════════════════════════════
# Camera Input
# ═══════════════════════════════════════
camera_image = st.camera_input("📷 التقط صورة")

if camera_image:
    image = Image.open(camera_image)

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
            <p style='color:#1a2744; font-weight:700; font-size:1rem; margin-bottom:8px;'>
                📷 الصورة الملتقطة
            </p>
        """, unsafe_allow_html=True)
        st.image(image, use_column_width=True)

    with col2:
        st.markdown("""
            <p style='color:#1a2744; font-weight:700; font-size:1rem; margin-bottom:8px;'>
                🔍 نتيجة التحليل
            </p>
        """, unsafe_allow_html=True)

        with st.spinner("جاري التحليل..."):
            pil_image = preprocess_frame(image)
            label, confidence, all_scores = predict_image(pil_image)

        is_alert = check_alert(label, confidence, threshold)

        if is_alert:
            st.markdown("""
                <div style='
                    background:#fff0f0;
                    border-radius:12px;
                    border-right:5px solid #e74c3c;
                    padding:16px 20px;
                    margin-bottom:16px;
                '>
                    <span style='color:#c0392b; font-weight:700; font-size:1.1rem;'>
                        🚨 تم اكتشاف سلوك مشبوه!
                    </span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='
                    background:#edfaf3;
                    border-radius:12px;
                    border-right:5px solid #27ae60;
                    padding:16px 20px;
                    margin-bottom:16px;
                '>
                    <span style='color:#1a7a4a; font-weight:700; font-size:1.1rem;'>
                        ✅ لا يوجد سلوك مشبوه
                    </span>
                </div>
            """, unsafe_allow_html=True)

        m1, m2 = st.columns(2)
        with m1:
            st.metric("السلوك المكتشف", label.upper())
        with m2:
            st.metric("نسبة الثقة", f"{confidence:.2%}")

        st.divider()

        st.markdown("""
            <p style='color:#1a2744; font-weight:700; font-size:0.95rem; margin-bottom:8px;'>
                📊 نسب كل السلوكيات
            </p>
        """, unsafe_allow_html=True)

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

        st.markdown("""
            <p style='color:#1a2744; font-weight:700; font-size:1rem; margin-bottom:12px;'>
                📧 إجراءات التنبيه
            </p>
        """, unsafe_allow_html=True)

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
