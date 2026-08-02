# SafeWatch - app/components/sidebar.py

import streamlit as st
from pathlib import Path


def render_sidebar():
    with st.sidebar:
        # Logo
        logo_path = Path("app/assets/logo.png")
        if logo_path.exists():
            st.image(str(logo_path), width=150)

        st.title("🛡️ SafeWatch")
        st.caption("نظام كشف السلوك المشبوه")
        st.divider()

        st.markdown("### 📌 الصفحات")
        st.page_link("app/pages/image_test.py",  label="🖼️ اختبار صورة")
        st.page_link("app/pages/live_camera.py", label="📹 كاميرا مباشرة")
        st.divider()

        st.markdown("### ⚙️ الإعدادات")
        threshold = st.slider(
            "حد التنبيه",
            min_value=0.5,
            max_value=1.0,
            value=0.75,
            step=0.05
        )
        st.session_state["threshold"] = threshold
        st.divider()

        st.caption("SafeWatch v1.0 — 2026")
