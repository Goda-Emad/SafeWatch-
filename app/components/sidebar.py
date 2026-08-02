# ActionLens - app/components/sidebar.py
import streamlit as st

TRANSLATIONS = {
    "ar": {
        "brand_sub":    "نظام التعرف على الحركة",
        "nav_home":     "🏠  الرئيسية",
        "nav_image":    "🖼️  رفع صورة",
        "nav_camera":   "📹  كاميرا لايف",
        "stat_analyses":"🔍 تحليلات",
        "stat_actions": "🎯 إجراءات",
        "stat_alerts":  "🚨 تنبيهات",
        "dark_toggle":  "☀️ فاتح",
        "light_toggle": "🌙 داكن",
        "lang_btn":     "🌐 English",
        "nav_label":    "القائمة",
        "stats_label":  "إحصائيات الجلسة",
        "footer_sub":   "التعرف على الحركة بالذكاء الاصطناعي",
    },
    "en": {
        "brand_sub":    "Action Recognition System",
        "nav_home":     "🏠  Home",
        "nav_image":    "🖼️  Upload Image",
        "nav_camera":   "📹  Live Camera",
        "stat_analyses":"🔍 Analyses",
        "stat_actions": "🎯 Actions",
        "stat_alerts":  "🚨 Alerts",
        "dark_toggle":  "☀️ Light",
        "light_toggle": "🌙 Dark",
        "lang_btn":     "🌐 العربية",
        "nav_label":    "NAVIGATION",
        "stats_label":  "SESSION STATS",
        "footer_sub":   "AI-Powered Action Recognition",
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

    if dark:
        BG_TOP  = "#0d1117"; BG_BOT  = "#0a0e15"
        BTN_BG  = "#161b27"; BTN_HVR = "#1e2535"; BTN_TXT = "#c9d1e0"
        ACT_BG  = "#0f1f15"; DIVIDER = "#1e2535"
        LABEL   = "#4a5568"; FOOT    = "#4a5568"
        APP_BG  = "#0a0e15"; CARD_BG = "#111622"; CARD_BOR= "#1e2535"
    else:
        BG_TOP  = "#f8fafc"; BG_BOT  = "#eef2f7"
        BTN_BG  = "#eef2f7"; BTN_HVR = "#e2e8f0"; BTN_TXT = "#1a2744"
        ACT_BG  = "#f0fff5"; DIVIDER = "#dce3ed"
        LABEL   = "#94a3b8"; FOOT    = "#94a3b8"
        APP_BG  = "#eef2f7"; CARD_BG = "#ffffff"; CARD_BOR= "#dce3ed"

    GREEN = "#63d28c"
    BLUE  = "#4f8ef7"
    RING  = "rgba(99,210,140,0.18)"

    # ── CSS: شيل كل margins الافتراضية من Streamlit ──
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {BG_TOP} 0%, {BG_BOT} 100%) !important;
        border-right: 1px solid {DIVIDER} !important;
        font-family: 'Cairo', sans-serif !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    [data-testid="stSidebar"] * {{ font-family: 'Cairo', sans-serif !important; }}

    /* إزالة gaps الزيادة بين العناصر */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div {{
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }}
    [data-testid="stSidebar"] .element-container {{
        margin-bottom: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown {{
        margin-bottom: 0 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown p {{
        margin: 0 !important;
        padding: 0 !important;
    }}

    /* أزرار nav */
    [data-testid="stSidebar"] .stButton > button {{
        background: {BTN_BG} !important;
        color: {BTN_TXT} !important;
        border: 1px solid {DIVIDER} !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 12px 16px !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        margin-bottom: 0 !important;
        transition: all 0.18s ease !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BTN_HVR} !important;
        color: {GREEN} !important;
        border-color: {GREEN}55 !important;
    }}
    [data-testid="stSidebar"] .stButton {{
        margin-bottom: 5px !important;
    }}

    /* active */
    .al-active .stButton > button {{
        background: {ACT_BG} !important;
        color: {GREEN} !important;
        border: 1px solid {GREEN}44 !important;
        border-left: 3px solid {GREEN} !important;
        font-weight: 700 !important;
    }}

    /* toggle أزرار أصغر */
    .al-toggle .stButton > button {{
        font-size: 0.78rem !important;
        padding: 8px 6px !important;
        border-radius: 8px !important;
    }}
    .al-toggle .stButton > button:hover {{
        color: {GREEN} !important;
        border-color: {GREEN}55 !important;
    }}
    .al-toggle .stButton {{
        margin-bottom: 0 !important;
    }}

    /* columns gap */
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        gap: 6px !important;
        margin-bottom: 0 !important;
    }}

    .stApp {{ background: {APP_BG} !important; }}
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:

        # ── Toggles ──
        tc1, tc2 = st.columns(2)
        with tc1:
            st.markdown('<div class="al-toggle">', unsafe_allow_html=True)
            lbl = t["dark_toggle"] if dark else t["light_toggle"]
            if st.button(lbl, key="toggle_dark", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with tc2:
            st.markdown('<div class="al-toggle">', unsafe_allow_html=True)
            if st.button(t["lang_btn"], key="toggle_lang", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # ── Brand + dividers مدمجة ──
        st.markdown(f"""
        <div style="margin:14px 0 0;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:16px;"></div>
            <div style="display:flex;align-items:center;gap:13px;padding:0 2px 16px;">
                <div style="display:flex;align-items:center;justify-content:center;
                            width:48px;height:48px;border-radius:13px;flex-shrink:0;
                            background:linear-gradient(135deg,{GREEN}25,{BLUE}25);
                            border:1px solid {GREEN}40;
                            box-shadow:0 0 0 4px {RING};
                            font-size:1.5rem;">🎯</div>
                <div>
                    <div style="font-size:1.12rem;font-weight:800;line-height:1.2;
                                background:linear-gradient(90deg,{GREEN},{BLUE});
                                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                        ActionLens
                    </div>
                    <div style="font-size:0.63rem;color:{LABEL};letter-spacing:1.4px;
                                text-transform:uppercase;margin-top:2px;">{t["brand_sub"]}</div>
                </div>
            </div>
            <div style="height:1px;background:{DIVIDER};margin-bottom:10px;"></div>
            <div style="font-size:0.6rem;color:{LABEL};font-weight:700;
                        letter-spacing:2px;text-transform:uppercase;
                        padding:0 2px;margin-bottom:8px;">{t["nav_label"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Navigation ──
        def nav_btn(label, key, page, target):
            active = st.session_state.get("active_page") == page
            st.markdown(f'<div class="{"al-active" if active else ""}">', unsafe_allow_html=True)
            if st.button(label, key=key, use_container_width=True):
                st.session_state["active_page"] = page
                st.switch_page(target)
            st.markdown('</div>', unsafe_allow_html=True)

        nav_btn(t["nav_home"],   "nav_home",   "home",   "app.py")
        nav_btn(t["nav_image"],  "nav_image",  "image",  "pages/image_test.py")
        nav_btn(t["nav_camera"], "nav_camera", "camera", "pages/live_camera.py")

        # ── Stats section ──
        analyses = st.session_state.get("total_predictions", 0)
        actions  = st.session_state.get("top_action", "—")
        alerts   = st.session_state.get("total_alerts", 0)

        st.markdown(f"""
        <div style="margin-top:14px;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:10px;"></div>
            <div style="font-size:0.6rem;color:{LABEL};font-weight:700;
                        letter-spacing:2px;text-transform:uppercase;
                        padding:0 2px;margin-bottom:8px;">{t["stats_label"]}</div>
            <div style="display:flex;flex-direction:column;gap:6px;">
                <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                            padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                    <span style="color:{LABEL};font-size:0.82rem;">{t["stat_analyses"]}</span>
                    <span style="color:{GREEN};font-weight:700;font-size:1rem;">{analyses}</span>
                </div>
                <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                            padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                    <span style="color:{LABEL};font-size:0.82rem;">{t["stat_actions"]}</span>
                    <span style="color:{BLUE};font-weight:700;font-size:1rem;">{actions}</span>
                </div>
                <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                            padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                    <span style="color:{LABEL};font-size:0.82rem;">{t["stat_alerts"]}</span>
                    <span style="color:#e74c3c;font-weight:700;font-size:1rem;">{alerts}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Footer ──
        st.markdown(f"""
        <div style="margin-top:20px;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:12px;"></div>
            <div style="text-align:center;">
                <div style="font-size:0.7rem;color:{FOOT};font-weight:600;margin-bottom:4px;">
                    🎯 ActionLens · 2026
                </div>
                <div style="font-size:0.63rem;color:{LABEL};">{t["footer_sub"]}</div>
                <div style="margin-top:8px;font-size:0.68rem;">
                    <a href="#" style="color:{GREEN};text-decoration:none;font-weight:600;">GitHub</a>
                    <span style="color:{DIVIDER};margin:0 6px;">·</span>
                    <a href="#" style="color:{GREEN};text-decoration:none;font-weight:600;">LinkedIn</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
