# SafeWatch - app/app.py
import streamlit as st
from pathlib import Path

BASE = Path(__file__).parent

# ═══════════════════════════════════════
# Page Config
# ═══════════════════════════════════════
st.set_page_config(
    page_title="SafeWatch — الرئيسية",
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
    st.markdown("""
        <div style='text-align:center; padding: 10px 0 4px;'>
            <span style='font-size:2.8rem;'>🛡️</span>
            <h2 style='color:#f0a500; margin:4px 0 0;'>SafeWatch</h2>
            <p style='color:#8a9bb5; font-size:0.8rem; margin:0;'>
                نظام كشف السلوك المشبوه
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📌 الصفحات")
    st.page_link("app.py",              label="🏠 الرئيسية")
    st.page_link("pages/image_test.py", label="🖼️ اختبار صورة")
    st.page_link("pages/live_camera.py",label="📹 كاميرا مباشرة")

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
# Hero Section
# ═══════════════════════════════════════
st.markdown("""
    <div style='
        background: linear-gradient(135deg, #1a2744 0%, #243358 100%);
        border-radius: 18px;
        padding: 40px 36px;
        margin-bottom: 28px;
        border-left: 5px solid #f0a500;
        box-shadow: 0 4px 24px rgba(26,39,68,0.13);
    '>
        <h1 style='
            color: #f0a500;
            font-size: 2.4rem;
            margin: 0 0 8px;
            border: none;
        '>🛡️ SafeWatch</h1>
        <p style='
            color: #c8d4e8;
            font-size: 1.1rem;
            margin: 0;
        '>نظام كشف السلوك المشبوه في الوقت الفعلي</p>
    </div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════
# Stats Row
# ═══════════════════════════════════════
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

# ═══════════════════════════════════════
# Cards Section
# ═══════════════════════════════════════
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div style='
            background: #ffffff;
            border-radius: 16px;
            padding: 28px;
            border: 1px solid #dce3ed;
            border-top: 4px solid #f0a500;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            height: 100%;
        '>
            <h3 style='color:#1a2744; margin-top:0;'>🖼️ اختبار صورة</h3>
            <p style='color:#5a6a85;'>ارفع صورة وحلل السلوك فيها فوراً.</p>
            <ul style='color:#5a6a85; padding-right:18px;'>
                <li>كشف السلوك المشبوه</li>
                <li>عرض نسبة الثقة</li>
                <li>إرسال تنبيه تلقائي</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/image_test.py", label="ابدأ الاختبار ←")

with col_b:
    st.markdown("""
        <div style='
            background: #ffffff;
            border-radius: 16px;
            padding: 28px;
            border: 1px solid #dce3ed;
            border-top: 4px solid #1a2744;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            height: 100%;
        '>
            <h3 style='color:#1a2744; margin-top:0;'>📹 كاميرا مباشرة</h3>
            <p style='color:#5a6a85;'>راقب عبر الكاميرا في الوقت الفعلي.</p>
            <ul style='color:#5a6a85; padding-right:18px;'>
                <li>مراقبة مستمرة</li>
                <li>تنبيه فوري</li>
                <li>تسجيل الحوادث</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/live_camera.py", label="شغّل الكاميرا ←")
