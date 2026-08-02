# SafeWatch - app/app.py
import streamlit as st
from pathlib import Path

BASE = Path(__file__).parent

# ═══════════════════════════════════════
# Page Config
# ═══════════════════════════════════════
st.set_page_config(
    page_title="SafeWatch",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════
# Load CSS
# ═══════════════════════════════════════
def load_css():
    css_path = BASE / "assets" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ═══════════════════════════════════════
# Sidebar
# ═══════════════════════════════════════
with st.sidebar:
    # Logo
    logo_path = BASE / "assets" / "logo.png"
    if logo_path.exists():
        try:
            st.image(str(logo_path), width=150)
        except Exception:
            st.title("🛡️")

    st.title("🛡️ SafeWatch")
    st.caption("نظام كشف السلوك المشبوه")
    st.divider()

    st.markdown("### 📌 الصفحات")
    st.page_link("pages/image_test.py",  label="🖼️ اختبار صورة")
    st.page_link("pages/live_camera.py", label="📹 كاميرا مباشرة")
    st.divider()

    st.markdown("### ⚙️ الإعدادات")
    threshold = st.slider(
        "حد التنبيه (Threshold)",
        min_value=0.5,
        max_value=1.0,
        value=0.75,
        step=0.05
    )
    st.session_state["threshold"] = threshold
    st.divider()
    st.caption("SafeWatch v1.0 — 2026")

# ═══════════════════════════════════════
# الصفحة الرئيسية
# ═══════════════════════════════════════
st.title("🛡️ SafeWatch")
st.subheader("نظام كشف السلوك المشبوه في الوقت الفعلي")
st.divider()

# Stats Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="🔍 الصور المحللة",
        value=st.session_state.get("total_predictions", 0)
    )
with col2:
    st.metric(
        label="🚨 التنبيهات",
        value=st.session_state.get("total_alerts", 0)
    )
with col3:
    st.metric(
        label="⚙️ حد التنبيه",
        value=f"{st.session_state.get('threshold', 0.75):.0%}"
    )
with col4:
    st.metric(
        label="📧 إيميلات مرسلة",
        value=st.session_state.get("total_emails", 0)
    )

st.divider()

# الوصف
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    ### 🖼️ اختبار صورة
    ارفع صورة وحلل السلوك فيها فوراً.
    - كشف السلوك المشبوه
    - عرض نسبة الثقة
    - إرسال تنبيه تلقائي
    """)
    st.page_link("pages/image_test.py", label="ابدأ الاختبار ←")

with col_b:
    st.markdown("""
    ### 📹 كاميرا مباشرة
    راقب عبر الكاميرا في الوقت الفعلي.
    - مراقبة مستمرة
    - تنبيه فوري
    - تسجيل الحوادث
    """)
    st.page_link("pages/live_camera.py", label="شغّل الكاميرا ←")
