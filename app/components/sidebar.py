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

    # ── Palette ──────────────────────────────────────────────
    if dark:
        BG       = "#0d1117"
        BTN_BG   = "#161b27"
        BTN_HVR  = "#1e2535"
        BTN_TXT  = "#c9d1e0"
        ACT_BG   = "#0f1f15"
        DIVIDER  = "#1e2535"
        LABEL    = "#4a5568"
        CARD_BG  = "#111622"
        CARD_BOR = "#1e2535"
        APP_BG   = "#0a0e15"
        SHADOW   = "rgba(0,0,0,0.4)"
    else:
        BG       = "#f0f4f8"
        BTN_BG   = "#ffffff"
        BTN_HVR  = "#e8edf5"
        BTN_TXT  = "#1a2744"
        ACT_BG   = "#f0fff5"
        DIVIDER  = "#dce3ed"
        LABEL    = "#94a3b8"
        CARD_BG  = "#ffffff"
        CARD_BOR = "#dce3ed"
        APP_BG   = "#eef2f7"
        SHADOW   = "rgba(0,0,0,0.08)"

    GREEN = "#63d28c"
    BLUE  = "#4f8ef7"

    analyses = st.session_state.get("total_predictions", 0)
    actions  = st.session_state.get("top_action", "—")
    alerts   = st.session_state.get("total_alerts", 0)

    page     = st.session_state.get("active_page", "home")
    home_act  = "al-active" if page == "home"   else ""
    img_act   = "al-active" if page == "image"  else ""
    cam_act   = "al-active" if page == "camera" else ""

    # ── Global CSS ───────────────────────────────────────────
    # كل شيء هنا: sidebar styling + button overrides
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    /* ===== Sidebar wrapper ===== */
    [data-testid="stSidebar"] > div:first-child {{
        background: {BG} !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] {{
        background: {BG} !important;
        border-right: 1px solid {DIVIDER} !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}

    /* ===== Kill ALL default Streamlit spacing inside sidebar ===== */
    [data-testid="stSidebar"] section[data-testid="stSidebarContent"] {{
        padding: 12px 12px 20px 12px !important;
        gap: 0 !important;
    }}
    [data-testid="stSidebar"] .block-container {{
        padding: 0 !important;
        gap: 0 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
        gap: 0 !important;
    }}
    [data-testid="stSidebar"] .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown > div {{
        margin: 0 !important;
        padding: 0 !important;
    }}

    /* ===== All sidebar fonts ===== */
    [data-testid="stSidebar"] * {{
        font-family: 'Cairo', sans-serif !important;
        box-sizing: border-box !important;
    }}

    /* ===== Buttons base ===== */
    [data-testid="stSidebar"] .stButton {{
        margin: 0 0 5px 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stButton > button {{
        background: {BTN_BG} !important;
        color: {BTN_TXT} !important;
        border: 1px solid {DIVIDER} !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 11px 14px !important;
        font-size: 0.90rem !important;
        font-weight: 600 !important;
        font-family: 'Cairo', sans-serif !important;
        text-align: center !important;
        transition: all 0.18s ease !important;
        box-shadow: none !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BTN_HVR} !important;
        color: {GREEN} !important;
        border-color: {GREEN}66 !important;
    }}

    /* ===== Active nav button ===== */
    .al-active [data-testid="stSidebar"] .stButton > button,
    [data-testid="stSidebar"] .al-active .stButton > button {{
        background: {ACT_BG} !important;
        color: {GREEN} !important;
        border: 1px solid {GREEN}55 !important;
        border-left: 3px solid {GREEN} !important;
        font-weight: 700 !important;
    }}

    /* ===== Toggle small buttons ===== */
    [data-testid="stSidebar"] .al-toggle .stButton > button {{
        font-size: 0.76rem !important;
        padding: 7px 6px !important;
        border-radius: 8px !important;
    }}
    [data-testid="stSidebar"] .al-toggle .stButton {{
        margin-bottom: 0 !important;
    }}

    /* ===== Columns gap ===== */
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        gap: 6px !important;
        margin: 0 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] > div {{
        padding: 0 !important;
        flex: 1 !important;
    }}

    /* ===== App background ===== */
    .stApp {{ background: {APP_BG} !important; }}
    </style>
    """, unsafe_allow_html=True)

    # ═══════════════════════════ SIDEBAR CONTENT ═══════════════
    with st.sidebar:

        # ── 1) Toggles row ──────────────────────────────────
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="al-toggle">', unsafe_allow_html=True)
            lbl = t["dark_toggle"] if dark else t["light_toggle"]
            if st.button(lbl, key="toggle_dark", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="al-toggle">', unsafe_allow_html=True)
            if st.button(t["lang_btn"], key="toggle_lang", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # ── 2) Brand block (HTML فقط - بدون containers زيادة) ──
        st.markdown(f"""
        <div style="padding:14px 0 0;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:14px;"></div>
            <div style="display:flex;align-items:center;gap:12px;padding:0 2px 14px;">
                <div style="width:46px;height:46px;border-radius:12px;flex-shrink:0;
                            display:flex;align-items:center;justify-content:center;
                            background:linear-gradient(135deg,{GREEN}22,{BLUE}22);
                            border:1px solid {GREEN}44;font-size:1.45rem;">🎯</div>
                <div>
                    <div style="font-size:1.1rem;font-weight:800;
                                background:linear-gradient(90deg,{GREEN},{BLUE});
                                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                        ActionLens
                    </div>
                    <div style="font-size:0.6rem;color:{LABEL};letter-spacing:1.4px;
                                text-transform:uppercase;margin-top:2px;">{t["brand_sub"]}</div>
                </div>
            </div>
            <div style="height:1px;background:{DIVIDER};margin-bottom:10px;"></div>
            <div style="font-size:0.58rem;color:{LABEL};font-weight:700;letter-spacing:2px;
                        text-transform:uppercase;margin-bottom:7px;">{t["nav_label"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── 3) Nav buttons ───────────────────────────────────
        def nav_btn(label, key, page_key, target):
            is_active = st.session_state.get("active_page") == page_key
            if is_active:
                st.markdown('<div class="al-active">', unsafe_allow_html=True)
            if st.button(label, key=key, use_container_width=True):
                st.session_state["active_page"] = page_key
                st.switch_page(target)
            if is_active:
                st.markdown('</div>', unsafe_allow_html=True)

        nav_btn(t["nav_home"],   "nav_home",   "home",   "app.py")
        nav_btn(t["nav_image"],  "nav_image",  "image",  "pages/image_test.py")
        nav_btn(t["nav_camera"], "nav_camera", "camera", "pages/live_camera.py")

        # ── 4) Stats + Footer (HTML واحد) ────────────────────
        st.markdown(f"""
        <div style="margin-top:12px;">
            <div style="height:1px;background:{DIVIDER};margin-bottom:10px;"></div>
            <div style="font-size:0.58rem;color:{LABEL};font-weight:700;letter-spacing:2px;
                        text-transform:uppercase;margin-bottom:8px;">{t["stats_label"]}</div>

            <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                        padding:10px 13px;margin-bottom:5px;
                        display:flex;justify-content:space-between;align-items:center;">
                <span style="color:{LABEL};font-size:0.82rem;">{t["stat_analyses"]}</span>
                <span style="color:{GREEN};font-weight:700;font-size:0.95rem;">{analyses}</span>
            </div>
            <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                        padding:10px 13px;margin-bottom:5px;
                        display:flex;justify-content:space-between;align-items:center;">
                <span style="color:{LABEL};font-size:0.82rem;">{t["stat_actions"]}</span>
                <span style="color:{BLUE};font-weight:700;font-size:0.95rem;">{actions}</span>
            </div>
            <div style="background:{CARD_BG};border:1px solid {CARD_BOR};border-radius:10px;
                        padding:10px 13px;margin-bottom:0;
                        display:flex;justify-content:space-between;align-items:center;">
                <span style="color:{LABEL};font-size:0.82rem;">{t["stat_alerts"]}</span>
                <span style="color:#e74c3c;font-weight:700;font-size:0.95rem;">{alerts}</span>
            </div>

            <div style="height:1px;background:{DIVIDER};margin:16px 0 12px;"></div>
            <div style="text-align:center;">
                <div style="font-size:0.68rem;color:{LABEL};font-weight:600;margin-bottom:3px;">
                    🎯 ActionLens · 2026
                </div>
                <div style="font-size:0.62rem;color:{LABEL};opacity:0.7;">{t["footer_sub"]}</div>
                <div style="margin-top:7px;font-size:0.66rem;">
                    <a href="#" style="color:{GREEN};text-decoration:none;font-weight:600;">GitHub</a>
                    <span style="color:{DIVIDER};margin:0 5px;">·</span>
                    <a href="#" style="color:{GREEN};text-decoration:none;font-weight:600;">LinkedIn</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
