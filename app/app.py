# ActionLens - app/app.py
import streamlit as st
import sys
from pathlib import Path

BASE = Path(__file__).parent
sys.path.append(str(BASE))

st.set_page_config(
    page_title="ActionLens — الرئيسية",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.sidebar import render_sidebar
st.session_state["active_page"] = "home"
render_sidebar()

dark = st.session_state.get("dark_mode", True)
lang = st.session_state.get("lang", "ar")

# ── Palette ──
if dark:
    PAGE_BG  = "#0a0e15"
    CARD_BG  = "#0d1117"
    CARD_BOR = "#1e2535"
    TEXT     = "#c9d1e0"
    SUB      = "#4a5568"
    MET_BG   = "#111622"
else:
    PAGE_BG  = "#eef2f7"
    CARD_BG  = "#ffffff"
    CARD_BOR = "#dce3ed"
    TEXT     = "#1a2744"
    SUB      = "#64748b"
    MET_BG   = "#f8fafc"

GREEN = "#63d28c"
BLUE  = "#4f8ef7"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
html, body, .stApp, [data-testid="stAppViewContainer"] {{
    background: {PAGE_BG} !important;
    font-family: 'Cairo', sans-serif !important;
}}
[data-testid="stMetric"] {{
    background: {MET_BG} !important;
    border: 1px solid {CARD_BOR} !important;
    border-radius: 12px !important;
    padding: 16px !important;
}}
[data-testid="stMetricLabel"] {{ color: {SUB} !important; font-size: 0.82rem !important; }}
[data-testid="stMetricValue"] {{ color: {TEXT} !important; font-weight: 700 !important; }}
hr {{ border-color: {CARD_BOR} !important; }}
.stButton > button {{
    background: {CARD_BG} !important;
    color: {TEXT} !important;
    border: 1px solid {CARD_BOR} !important;
    border-radius: 10px !important;
    font-family: 'Cairo', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.18s !important;
}}
.stButton > button:hover {{
    border-color: {GREEN}88 !important;
    color: {GREEN} !important;
}}
</style>
""", unsafe_allow_html=True)

# ── Hero ──
hero_sub = "نظام التعرف على الحركة البشرية بالذكاء الاصطناعي" if lang == "ar" else "AI-Powered Human Action Recognition System"
st.markdown(f"""
<div style="background:linear-gradient(135deg,{CARD_BG} 0%,{MET_BG} 100%);
            border-radius:18px;padding:36px 32px;margin-bottom:24px;
            border:1px solid {CARD_BOR};border-left:4px solid {GREEN};">
    <div style="font-size:2.2rem;font-weight:800;margin-bottom:8px;
                background:linear-gradient(90deg,{GREEN},{BLUE});
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
        🎯 ActionLens
    </div>
    <div style="color:{SUB};font-size:1rem;">{hero_sub}</div>
</div>
""", unsafe_allow_html=True)

# ── Stats ──
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🔍 تحليلات" if lang=="ar" else "🔍 Analyses",
              st.session_state.get("total_predictions", 0))
with col2:
    st.metric("🎯 آخر إجراء" if lang=="ar" else "🎯 Last Action",
              st.session_state.get("top_action", "—"))
with col3:
    st.metric("🚨 تنبيهات" if lang=="ar" else "🚨 Alerts",
              st.session_state.get("total_alerts", 0))

st.divider()

# ── Cards ──
lbl_img  = ("🖼️ رفع صورة",   "ارفع صورة وحلل الحركة فوراً.",     "ابدأ التحليل ←") if lang=="ar" else ("🖼️ Upload Image",  "Upload an image and detect actions instantly.", "Start →")
lbl_cam  = ("📹 كاميرا لايف", "راقب عبر الكاميرا في الوقت الفعلي.", "شغّل الكاميرا ←") if lang=="ar" else ("📹 Live Camera",   "Monitor via camera in real time.",              "Open Camera →")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"""
    <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:16px;
                padding:26px;border-top:3px solid {GREEN};margin-bottom:14px;">
        <div style="font-size:1.1rem;font-weight:700;color:{TEXT};margin-bottom:8px;">{lbl_img[0]}</div>
        <div style="color:{SUB};font-size:0.88rem;">{lbl_img[1]}</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(lbl_img[2], key="btn_image", use_container_width=True):
        st.switch_page("pages/image_test.py")

with col_b:
    st.markdown(f"""
    <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:16px;
                padding:26px;border-top:3px solid {BLUE};margin-bottom:14px;">
        <div style="font-size:1.1rem;font-weight:700;color:{TEXT};margin-bottom:8px;">{lbl_cam[0]}</div>
        <div style="color:{SUB};font-size:0.88rem;">{lbl_cam[1]}</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(lbl_cam[2], key="btn_camera", use_container_width=True):
        st.switch_page("pages/live_camera.py")
