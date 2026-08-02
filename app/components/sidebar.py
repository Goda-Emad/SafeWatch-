# SafeWatch - app/components/sidebar.py
import streamlit as st

# ═══════════════════════════════════════
# Translations
# ═══════════════════════════════════════
TRANSLATIONS = {
    "ar": {
        "brand_sub":    "نظام المراقبة الذكي",
        "nav_home":     "🏠  الرئيسية",
        "nav_image":    "🖼️  اختبار صورة",
        "nav_camera":   "📹  كاميرا مباشرة",
        "nav_alerts":   "🚨  التنبيهات",
        "nav_reports":  "📊  التقارير",
        "stat_analysis":"🔍 تحليلات",
        "stat_alerts":  "🚨 تنبيهات",
        "stat_emails":  "📧 إيميلات",
        "dark_toggle":  "☀️ Light",
        "light_toggle": "🌙 Dark",
        "lang_btn":     "🌐 English",
    },
    "en": {
        "brand_sub":    "Smart Surveillance System",
        "nav_home":     "🏠  Home",
        "nav_image":    "🖼️  Image Test",
        "nav_camera":   "📹  Live Camera",
        "nav_alerts":   "🚨  Alerts",
        "nav_reports":  "📊  Reports",
        "stat_analysis":"🔍 Analyses",
        "stat_alerts":  "🚨 Alerts",
        "stat_emails":  "📧 Emails",
        "dark_toggle":  "☀️ Light",
        "light_toggle": "🌙 Dark",
        "lang_btn":     "🌐 العربية",
    },
}


def _init_session():
    if "lang"        not in st.session_state: st.session_state["lang"]        = "ar"
    if "dark_mode"   not in st.session_state: st.session_state["dark_mode"]   = True
    if "active_page" not in st.session_state: st.session_state["active_page"] = "home"


def render_sidebar():
    _init_session()

    dark = st.session_state["dark_mode"]
    lang = st.session_state["lang"]
    t    = TRANSLATIONS[lang]

    # ── Colour palette ───────────────────────────────────────
    if dark:
        BG_TOP   = "#1a1a2e"
        BG_BOT   = "#0f0f1a"
        BTN_BG   = "#22223a"
        BTN_HVR  = "#2e2e50"
        BTN_TXT  = "#d0d0e8"
        ACT_BG   = "#2e2510"
        DIVIDER  = "#2e2e50"
        LABEL    = "#6060a0"
        FOOT     = "#505070"
        RING     = "rgba(240,165,0,0.25)"
        APP_BG   = "#0f0f1a"
    else:
        BG_TOP   = "#ffffff"
        BG_BOT   = "#f0f4f8"
        BTN_BG   = "#f0f4f8"
        BTN_HVR  = "#e2e8f0"
        BTN_TXT  = "#1a2744"
        ACT_BG   = "#fff8e6"
        DIVIDER  = "#dce3ed"
        LABEL    = "#8a9bb5"
        FOOT     = "#8a9bb5"
        RING     = "rgba(240,165,0,0.20)"
        APP_BG   = "#f0f4f8"

    GOLD = "#f0a500"

    # ── CSS ──────────────────────────────────────────────────
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {BG_TOP} 0%, {BG_BOT} 100%) !important;
        border-right: 1px solid {DIVIDER} !important;
        font-family: 'Cairo', sans-serif !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}

    [data-testid="stSidebar"] * {{
        font-family: 'Cairo', sans-serif !important;
    }}

    [data-testid="stSidebar"] .stButton > button {{
        background: {BTN_BG} !important;
        color: {BTN_TXT} !important;
        border: none !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 13px 18px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        font-family: 'Cairo', sans-serif !important;
        text-align: center !important;
        margin-bottom: 6px !important;
        transition: background 0.18s, color 0.18s !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BTN_HVR} !important;
        color: {GOLD} !important;
    }}

    /* active nav */
    .sw-active .stButton > button {{
        background: {ACT_BG} !important;
        color: {GOLD} !important;
        border-left: 3px solid {GOLD} !important;
        font-weight: 700 !important;
    }}

    /* small toggles */
    .sw-toggle .stButton > button {{
        font-size: 0.82rem !important;
        padding: 9px 10px !important;
        margin-bottom: 0 !important;
        border-radius: 8px !important;
    }}

    .stApp {{ background: {APP_BG} !important; }}
    </style>
    """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════
    with st.sidebar:

        # ── Top toggles ──────────────────────────────────────
        tc1, tc2 = st.columns(2)
        with tc1:
            st.markdown('<div class="sw-toggle">', unsafe_allow_html=True)
            if st.button(t["dark_toggle"] if dark else t["light_toggle"],
                         key="toggle_dark", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with tc2:
            st.markdown('<div class="sw-toggle">', unsafe_allow_html=True)
            if st.button(t["lang_btn"], key="toggle_lang", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'<div style="height:1px;background:{DIVIDER};margin:14px 0;"></div>',
                    unsafe_allow_html=True)

        # ── Brand ────────────────────────────────────────────
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:14px;padding:6px 4px 18px;">
            <div style="display:flex;align-items:center;justify-content:center;
                        width:52px;height:52px;border-radius:12px;
                        background:linear-gradient(135deg,{GOLD},{BG_TOP});
                        box-shadow:0 0 0 6px {RING};
                        font-size:1.7rem;flex-shrink:0;">🛡️</div>
            <div>
                <div style="font-size:1.15rem;font-weight:800;color:{GOLD};
                            letter-spacing:0.5px;line-height:1.2;">SafeWatch</div>
                <div style="font-size:0.68rem;color:{LABEL};letter-spacing:1.5px;
                            text-transform:uppercase;margin-top:2px;">{t["brand_sub"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div style="height:1px;background:{DIVIDER};margin-bottom:14px;"></div>',
                    unsafe_allow_html=True)

        # ── Navigation ───────────────────────────────────────
        def nav_btn(label, key, page, target):
            active = st.session_state.get("active_page") == page
            st.markdown(f'<div class="{"sw-active" if active else ""}">', unsafe_allow_html=True)
            if st.button(label, key=key, use_container_width=True):
                st.session_state["active_page"] = page
                st.switch_page(target)
            st.markdown('</div>', unsafe_allow_html=True)

        nav_btn(t["nav_home"],    "nav_home",    "home",    "app.py")
        nav_btn(t["nav_image"],   "nav_image",   "image",   "pages/image_test.py")
        nav_btn(t["nav_camera"],  "nav_camera",  "camera",  "pages/live_camera.py")
        nav_btn(t["nav_alerts"],  "nav_alerts",  "alerts",  "pages/alerts.py")
        nav_btn(t["nav_reports"], "nav_reports", "reports", "pages/reports.py")

        st.markdown(f'<div style="height:1px;background:{DIVIDER};margin:14px 0;"></div>',
                    unsafe_allow_html=True)

        # ── Stats ────────────────────────────────────────────
        predictions = st.session_state.get("total_predictions", 0)
        alerts      = st.session_state.get("total_alerts",      0)
        emails      = st.session_state.get("total_emails",      0)

        def stat_row(label, value, color):
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;
                        background:{BTN_BG};border-radius:10px;
                        padding:10px 14px;margin-bottom:6px;">
                <span style="color:{LABEL};font-size:0.83rem;">{label}</span>
                <span style="color:{color};font-weight:700;font-size:1rem;">{value}</span>
            </div>""", unsafe_allow_html=True)

        stat_row(t["stat_analysis"], predictions, GOLD)
        stat_row(t["stat_alerts"],   alerts,      "#e74c3c")
        stat_row(t["stat_emails"],   emails,      "#2ecc71")

        # ── Footer ───────────────────────────────────────────
        st.markdown(f"""
        <div style="margin-top:24px;text-align:center;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:12px;"></div>
            <div style="font-size:0.72rem;color:{FOOT};font-weight:600;">SafeWatch · 2026</div>
            <div style="font-size:0.7rem;margin-top:4px;">
                <a href="#" style="color:{GOLD};text-decoration:none;">GitHub</a>
                <span style="color:{DIVIDER};margin:0 6px;">·</span>
                <a href="#" style="color:{GOLD};text-decoration:none;">LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
