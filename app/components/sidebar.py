# SafeWatch - app/components/sidebar.py
import streamlit as st

def render_sidebar():

    NAVY   = "#1a2744"
    GOLD   = "#f0a500"
    BORDER = "#2a3a55"
    WHITE  = "#e8edf5"
    GREY   = "#8a9bb5"
    DARK   = "#0d1b2a"

    st.markdown(
        "<style>"
        "@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');"
        f"[data-testid='stSidebar']{{background:linear-gradient(180deg,{NAVY} 0%,{DARK} 100%)!important;border-right:2px solid {GOLD}!important;}}"
        "[data-testid='stSidebarNav']{display:none!important;}"
        f"[data-testid='stSidebar'] div,[data-testid='stSidebar'] span,"
        f"[data-testid='stSidebar'] p,[data-testid='stSidebar'] label{{color:{WHITE}!important;font-family:'Cairo',sans-serif!important;}}"
        "[data-testid='stSidebar'] .stButton>button{"
        f"background:transparent!important;border:1px solid {BORDER}!important;"
        f"color:{GREY}!important;border-radius:10px!important;"
        "width:100%!important;font-size:.88rem!important;font-weight:600!important;"
        "padding:10px 14px!important;margin-bottom:4px!important;transition:all .18s!important;"
        "text-align:right!important;}"
        "[data-testid='stSidebar'] .stButton>button:hover{"
        f"background:{GOLD}22!important;color:{GOLD}!important;border-color:{GOLD}66!important;}}"
        f".home-btn .stButton>button{{background:{GOLD}18!important;border:1px solid {GOLD}55!important;color:{GOLD}!important;font-weight:700!important;}}"
        f".home-btn .stButton>button:hover{{background:{GOLD}35!important;border-color:{GOLD}!important;}}"
        "</style>",
        unsafe_allow_html=True
    )

    with st.sidebar:

        # ── Brand ──
        st.markdown(
            f'<div style="text-align:center;padding:24px 0 16px;">'
            f'<div style="display:inline-flex;align-items:center;justify-content:center;'
            f'background:linear-gradient(135deg,{GOLD},{NAVY});'
            f'border-radius:50%;width:68px;height:68px;font-size:2.2rem;'
            f'box-shadow:0 4px 18px rgba(240,165,0,0.35);margin-bottom:12px;">🛡️</div>'
            f'<div style="font-size:1.4rem;font-weight:700;color:{GOLD};letter-spacing:1px;">SafeWatch</div>'
            f'<div style="font-size:0.7rem;color:{GREY};letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;">'
            f'Smart Surveillance System</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(f'<div style="height:1px;background:{BORDER};margin-bottom:14px;"></div>', unsafe_allow_html=True)

        # ── Navigation ──
        st.markdown(
            f'<div style="font-size:0.68rem;color:{GREY};font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;padding:0 4px;margin-bottom:8px;">'
            f'القائمة</div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="home-btn">', unsafe_allow_html=True)
        if st.button("🏠  الرئيسية", key="nav_home", use_container_width=True):
            st.switch_page("app.py")
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🖼️  اختبار صورة", key="nav_image", use_container_width=True):
            st.switch_page("pages/image_test.py")

        if st.button("📹  كاميرا مباشرة", key="nav_camera", use_container_width=True):
            st.switch_page("pages/live_camera.py")

        st.markdown(f'<div style="height:1px;background:{BORDER};margin:14px 0;"></div>', unsafe_allow_html=True)

        # ── Stats ──
        st.markdown(
            f'<div style="font-size:0.68rem;color:{GREY};font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;padding:0 4px;margin-bottom:10px;">'
            f'إحصائيات الجلسة</div>',
            unsafe_allow_html=True
        )

        predictions = st.session_state.get("total_predictions", 0)
        alerts      = st.session_state.get("total_alerts", 0)
        emails      = st.session_state.get("total_emails", 0)

        st.markdown(
            f'<div style="display:flex;flex-direction:column;gap:8px;">'

            f'<div style="background:{DARK};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {BORDER};">'
            f'<span style="color:{GREY};font-size:0.82rem;">🔍 تحليلات</span>'
            f'<span style="color:{GOLD};font-weight:700;font-size:1rem;">{predictions}</span></div>'

            f'<div style="background:{DARK};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {BORDER};">'
            f'<span style="color:{GREY};font-size:0.82rem;">🚨 تنبيهات</span>'
            f'<span style="color:#e74c3c;font-weight:700;font-size:1rem;">{alerts}</span></div>'

            f'<div style="background:{DARK};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {BORDER};">'
            f'<span style="color:{GREY};font-size:0.82rem;">📧 إيميلات</span>'
            f'<span style="color:#2ecc71;font-weight:700;font-size:1rem;">{emails}</span></div>'

            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(f'<div style="height:1px;background:{BORDER};margin:14px 0 8px;"></div>', unsafe_allow_html=True)

        # ── Footer ──
        st.markdown(
            f'<div style="font-size:0.68rem;color:{GREY};text-align:center;padding:0 2px;line-height:2;">'
            f'🛡️ SafeWatch v1.0 — 2026<br>'
            f'نظام المراقبة الذكي'
            f'</div>',
            unsafe_allow_html=True
        )
