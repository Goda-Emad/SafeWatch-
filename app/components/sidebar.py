# ActionLens - app/components/sidebar.py
import streamlit as st

TRANSLATIONS = {
    "ar": {
        "brand_sub":    "نظام التعرف على الحركة",
        "nav_home":     "🏠  الرئيسية",
        "nav_image":    "🖼️  رفع صورة",
        "nav_camera":   "📹  كاميرا لايف",
        "stat_analyses": "🔍 تحليلات",
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
        "stat_analyses": "🔍 Analyses",
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
    """تهيئة متغيرات الجلسة"""
    if "lang" not in st.session_state:
        st.session_state["lang"] = "ar"
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = True
    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "home"
    if "total_predictions" not in st.session_state:
        st.session_state["total_predictions"] = 0
    if "top_action" not in st.session_state:
        st.session_state["top_action"] = "—"
    if "total_alerts" not in st.session_state:
        st.session_state["total_alerts"] = 0


def render_sidebar():
    """عرض الشريط الجانبي"""
    _init_session()

    dark = st.session_state["dark_mode"]
    lang = st.session_state["lang"]
    t = TRANSLATIONS[lang]

    # ── تحديد الألوان حسب الوضع (داكن / فاتح) ──
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
    RED   = "#e74c3c"

    # ── جلب البيانات من الجلسة ──
    analyses = st.session_state.get("total_predictions", 0)
    actions  = st.session_state.get("top_action", "—")
    alerts   = st.session_state.get("total_alerts", 0)
    page     = st.session_state.get("active_page", "home")

    # ── CSS التنسيقات العامة ──
    st.markdown(f"""
    <style>
    /* ===== تنسيق الـ Sidebar ===== */
    [data-testid="stSidebar"] > div:first-child {{
        background: {BG} !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] {{
        background: {BG} !important;
        border-right: 1px solid {DIVIDER} !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    
    /* ===== إزالة المسافات الداخلية ===== */
    [data-testid="stSidebar"] section[data-testid="stSidebarContent"] {{
        padding: 12px 12px 20px 12px !important;
    }}
    [data-testid="stSidebar"] .block-container {{
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    
    /* ===== الخطوط ===== */
    [data-testid="stSidebar"] * {{
        font-family: 'Cairo', 'Segoe UI', sans-serif !important;
    }}
    
    /* ===== الأزرار ===== */
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
        text-align: center !important;
        transition: all 0.18s ease !important;
        box-shadow: none !important;
        height: auto !important;
        line-height: 1.4 !important;
        white-space: normal !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BTN_HVR} !important;
        color: {GREEN} !important;
        border-color: {GREEN}66 !important;
    }}
    
    /* ===== الزر النشط ===== */
    .nav-active .stButton > button {{
        background: {ACT_BG} !important;
        color: {GREEN} !important;
        border: 1px solid {GREEN}55 !important;
        border-left: 3px solid {GREEN} !important;
        font-weight: 700 !important;
    }}
    
    /* ===== أزرار التبديل الصغيرة ===== */
    .toggle-btn .stButton > button {{
        font-size: 0.76rem !important;
        padding: 7px 6px !important;
        border-radius: 8px !important;
    }}
    .toggle-btn .stButton {{
        margin-bottom: 0 !important;
    }}
    
    /* ===== الأعمدة ===== */
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        gap: 6px !important;
        margin: 0 0 5px 0 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] > div {{
        padding: 0 !important;
        flex: 1 !important;
    }}
    
    /* ===== خلفية التطبيق ===== */
    .stApp {{ background: {APP_BG} !important; }}
    
    /* ===== تنسيق البطاقات الإحصائية ===== */
    .stat-card {{
        background: {CARD_BG};
        border: 1px solid {CARD_BOR};
        border-radius: 10px;
        padding: 10px 13px;
        margin-bottom: 5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .stat-label {{
        color: {LABEL};
        font-size: 0.82rem;
    }}
    .stat-value-green {{
        color: {GREEN};
        font-weight: 700;
        font-size: 0.95rem;
    }}
    .stat-value-blue {{
        color: {BLUE};
        font-weight: 700;
        font-size: 0.95rem;
    }}
    .stat-value-red {{
        color: {RED};
        font-weight: 700;
        font-size: 0.95rem;
    }}
    
    /* ===== العلامة التجارية ===== */
    .brand-container {{
        padding: 8px 0 10px 0;
    }}
    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 2px 12px 2px;
    }}
    .brand-icon {{
        width: 46px;
        height: 46px;
        border-radius: 12px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, {GREEN}22, {BLUE}22);
        border: 1px solid {GREEN}44;
        font-size: 1.45rem;
    }}
    .brand-title {{
        font-size: 1.1rem;
        font-weight: 800;
        background: linear-gradient(90deg, {GREEN}, {BLUE});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    .brand-sub {{
        font-size: 0.6rem;
        color: {LABEL};
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin-top: 2px;
    }}
    
    /* ===== التسميات ===== */
    .section-label {{
        font-size: 0.58rem;
        color: {LABEL};
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 10px 0 7px 0;
    }}
    
    /* ===== الفاصل ===== */
    .divider {{
        height: 1px;
        background: {DIVIDER};
        margin: 8px 0;
    }}
    
    /* ===== التذييل ===== */
    .footer {{
        text-align: center;
        margin-top: 15px;
        padding-top: 12px;
        border-top: 1px solid {DIVIDER};
    }}
    .footer-title {{
        font-size: 0.68rem;
        color: {LABEL};
        font-weight: 600;
        margin-bottom: 3px;
    }}
    .footer-sub {{
        font-size: 0.62rem;
        color: {LABEL};
        opacity: 0.7;
    }}
    .footer-links {{
        margin-top: 7px;
        font-size: 0.66rem;
    }}
    .footer-links a {{
        color: {GREEN};
        text-decoration: none;
        font-weight: 600;
    }}
    .footer-links a:hover {{
        text-decoration: underline;
    }}
    .footer-links span {{
        color: {DIVIDER};
        margin: 0 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ── عرض محتوى الـ Sidebar ──
    with st.sidebar:

        # ── 1) أزرار التبديل (الوضع الداكن / اللغة) ──
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="toggle-btn">', unsafe_allow_html=True)
            toggle_label = t["dark_toggle"] if dark else t["light_toggle"]
            if st.button(toggle_label, key="toggle_dark", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="toggle-btn">', unsafe_allow_html=True)
            if st.button(t["lang_btn"], key="toggle_lang", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # ── 2) العلامة التجارية (Brand) ──
        st.markdown(f"""
        <div class="brand-container">
            <div class="divider"></div>
            <div class="brand">
                <div class="brand-icon">🎯</div>
                <div>
                    <div class="brand-title">ActionLens</div>
                    <div class="brand-sub">{t["brand_sub"]}</div>
                </div>
            </div>
            <div class="divider" style="margin-bottom:10px;"></div>
            <div class="section-label">{t["nav_label"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── 3) أزرار التنقل ──
        nav_items = {
            "home": {"label": t["nav_home"], "target": "app.py"},
            "image": {"label": t["nav_image"], "target": "pages/image_test.py"},
            "camera": {"label": t["nav_camera"], "target": "pages/live_camera.py"},
        }

        for key, item in nav_items.items():
            is_active = (page == key)
            if is_active:
                st.markdown('<div class="nav-active">', unsafe_allow_html=True)
            
            if st.button(item["label"], key=f"nav_{key}", use_container_width=True):
                st.session_state["active_page"] = key
                st.switch_page(item["target"])
            
            if is_active:
                st.markdown('</div>', unsafe_allow_html=True)

        # ── 4) الإحصائيات والتذييل ──
        st.markdown(f"""
        <div style="margin-top:12px;">
            <div class="divider" style="margin-bottom:10px;"></div>
            <div class="section-label" style="margin-top:0;">{t["stats_label"]}</div>
            
            <div class="stat-card">
                <span class="stat-label">{t["stat_analyses"]}</span>
                <span class="stat-value-green">{analyses}</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">{t["stat_actions"]}</span>
                <span class="stat-value-blue">{actions}</span>
            </div>
            <div class="stat-card" style="margin-bottom:0;">
                <span class="stat-label">{t["stat_alerts"]}</span>
                <span class="stat-value-red">{alerts}</span>
            </div>
            
            <div class="footer">
                <div class="footer-title">🎯 ActionLens · 2026</div>
                <div class="footer-sub">{t["footer_sub"]}</div>
                <div class="footer-links">
                    <a href="https://github.com" target="_blank">GitHub</a>
                    <span>·</span>
                    <a href="https://linkedin.com" target="_blank">LinkedIn</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
