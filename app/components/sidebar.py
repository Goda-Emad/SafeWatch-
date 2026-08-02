# ActionLens - app/components/sidebar.py
import streamlit as st

TRANSLATIONS = {
    "ar": {
        "brand_sub": "نظام التعرف على الحركة",
        "nav_home": "🏠 الرئيسية",
        "nav_image": "🖼️ رفع صورة",
        "nav_camera": "📹 كاميرا لايف",
        "stat_analyses": "🔍 تحليلات",
        "stat_actions": "🎯 إجراءات",
        "stat_alerts": "🚨 تنبيهات",
        "dark_toggle": "☀️ فاتح",
        "light_toggle": "🌙 داكن",
        "lang_btn": "🌐 English",
        "nav_label": "القائمة",
        "stats_label": "إحصائيات الجلسة",
        "footer_sub": "التعرف على الحركة بالذكاء الاصطناعي",
    },
    "en": {
        "brand_sub": "Action Recognition System",
        "nav_home": "🏠 Home",
        "nav_image": "🖼️ Upload Image",
        "nav_camera": "📹 Live Camera",
        "stat_analyses": "🔍 Analyses",
        "stat_actions": "🎯 Actions",
        "stat_alerts": "🚨 Alerts",
        "dark_toggle": "☀️ Light",
        "light_toggle": "🌙 Dark",
        "lang_btn": "🌐 العربية",
        "nav_label": "NAVIGATION",
        "stats_label": "SESSION STATS",
        "footer_sub": "AI-Powered Action Recognition",
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
        BG = "#0d1117"
        CARD_BG = "#161b22"
        CARD_BORDER = "#30363d"
        TEXT_COLOR = "#c9d1d9"
        LABEL_COLOR = "#8b949e"
        GREEN = "#58a6ff"
        BLUE = "#58a6ff"
        RED = "#f85149"
        BUTTON_BG = "#21262d"
        BUTTON_HOVER = "#30363d"
        DIVIDER = "#30363d"
        ACTIVE_BG = "#0d1f2d"
    else:
        BG = "#ffffff"
        CARD_BG = "#f6f8fa"
        CARD_BORDER = "#d0d7de"
        TEXT_COLOR = "#24292f"
        LABEL_COLOR = "#57606a"
        GREEN = "#2da44e"
        BLUE = "#0969da"
        RED = "#cf222e"
        BUTTON_BG = "#f6f8fa"
        BUTTON_HOVER = "#f3f4f6"
        DIVIDER = "#d0d7de"
        ACTIVE_BG = "#ddf4ff"

    # ── جلب البيانات من الجلسة ──
    analyses = st.session_state.get("total_predictions", 0)
    actions = st.session_state.get("top_action", "—")
    alerts = st.session_state.get("total_alerts", 0)
    page = st.session_state.get("active_page", "home")

    # ── CSS التنسيقات العامة ──
    st.markdown(f"""
    <style>
    /* ===== تنسيق الـ Sidebar ===== */
    [data-testid="stSidebar"] {{
        background: {BG} !important;
        border-right: 1px solid {DIVIDER} !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background: {BG} !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebarNav"] {{
        display: none !important;
    }}
    
    /* ===== إزالة المسافات الداخلية ===== */
    [data-testid="stSidebar"] section[data-testid="stSidebarContent"] {{
        padding: 1rem 1rem 2rem 1rem !important;
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
        font-family: 'Segoe UI', 'Cairo', sans-serif !important;
    }}
    
    /* ===== الأزرار ===== */
    [data-testid="stSidebar"] .stButton {{
        margin: 0 0 6px 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stButton > button {{
        background: {BUTTON_BG} !important;
        color: {TEXT_COLOR} !important;
        border: 1px solid {CARD_BORDER} !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 0.6rem 1rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        height: auto !important;
        line-height: 1.5 !important;
        white-space: normal !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BUTTON_HOVER} !important;
        border-color: {GREEN} !important;
        color: {GREEN} !important;
        transform: translateY(-1px);
    }}
    [data-testid="stSidebar"] .stButton > button:active {{
        transform: translateY(0px);
    }}
    
    /* ===== الزر النشط ===== */
    .nav-active .stButton > button {{
        background: {ACTIVE_BG} !important;
        color: {GREEN} !important;
        border: 1px solid {GREEN} !important;
        border-left: 4px solid {GREEN} !important;
        font-weight: 700 !important;
    }}
    
    /* ===== أزرار التبديل الصغيرة ===== */
    .toggle-btn .stButton > button {{
        font-size: 0.75rem !important;
        padding: 0.4rem 0.5rem !important;
        border-radius: 6px !important;
    }}
    .toggle-btn .stButton {{
        margin-bottom: 0 !important;
    }}
    
    /* ===== الأعمدة ===== */
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        gap: 8px !important;
        margin: 0 0 6px 0 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] > div {{
        padding: 0 !important;
        flex: 1 !important;
    }}
    
    /* ===== خلفية التطبيق ===== */
    .stApp {{
        background: {BG} !important;
    }}
    
    /* ===== تنسيق البطاقات الإحصائية ===== */
    .stat-card {{
        background: {CARD_BG};
        border: 1px solid {CARD_BORDER};
        border-radius: 8px;
        padding: 0.7rem 1rem;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.2s ease;
    }}
    .stat-card:hover {{
        border-color: {GREEN};
        transform: translateX(4px);
    }}
    .stat-label {{
        color: {LABEL_COLOR};
        font-size: 0.85rem;
        font-weight: 500;
    }}
    .stat-value {{
        font-weight: 700;
        font-size: 1rem;
    }}
    .stat-green {{ 
        color: {GREEN};
    }}
    .stat-blue {{ 
        color: {BLUE};
    }}
    .stat-red {{ 
        color: {RED};
    }}
    
    /* ===== العلامة التجارية ===== */
    .brand-container {{
        padding: 4px 0 8px 0;
    }}
    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0 12px 0;
    }}
    .brand-icon {{
        font-size: 2.2rem;
        line-height: 1;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }}
    .brand-title {{
        font-size: 1.4rem;
        font-weight: 800;
        color: {TEXT_COLOR};
        letter-spacing: -0.5px;
    }}
    .brand-sub {{
        font-size: 0.6rem;
        color: {LABEL_COLOR};
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 2px;
        font-weight: 600;
    }}
    
    /* ===== التسميات ===== */
    .section-label {{
        font-size: 0.6rem;
        color: {LABEL_COLOR};
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 1.2rem 0 0.6rem 0;
    }}
    
    /* ===== الفاصل ===== */
    .divider {{
        height: 1px;
        background: {DIVIDER};
        margin: 0.6rem 0;
    }}
    
    /* ===== التذييل ===== */
    .footer {{
        text-align: center;
        margin-top: 1.5rem;
        padding-top: 1rem;
        border-top: 1px solid {DIVIDER};
    }}
    .footer-title {{
        font-size: 0.75rem;
        color: {TEXT_COLOR};
        font-weight: 600;
        margin-bottom: 4px;
    }}
    .footer-sub {{
        font-size: 0.6rem;
        color: {LABEL_COLOR};
        margin-bottom: 6px;
    }}
    .footer-links {{
        margin-top: 6px;
        display: flex;
        justify-content: center;
        gap: 12px;
    }}
    .footer-links a {{
        color: {GREEN};
        text-decoration: none;
        font-size: 0.7rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .footer-links a:hover {{
        text-decoration: underline;
        opacity: 0.8;
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
            <div class="brand">
                <div class="brand-icon">🎯</div>
                <div>
                    <div class="brand-title">ActionLens</div>
                    <div class="brand-sub">{t["brand_sub"]}</div>
                </div>
            </div>
            <div class="divider"></div>
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
                try:
                    st.switch_page(item["target"])
                except Exception as e:
                    st.error(f"خطأ في التنقل إلى {item['target']}: {e}")
            
            if is_active:
                st.markdown('</div>', unsafe_allow_html=True)

        # ── 4) الإحصائيات ──
        st.markdown(f"""
        <div style="margin-top: 0.5rem;">
            <div class="section-label" style="margin-top: 0;">{t["stats_label"]}</div>
            
            <div class="stat-card">
                <span class="stat-label">{t["stat_analyses"]}</span>
                <span class="stat-value stat-green">{analyses}</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">{t["stat_actions"]}</span>
                <span class="stat-value stat-blue">{actions}</span>
            </div>
            <div class="stat-card" style="margin-bottom: 0;">
                <span class="stat-label">{t["stat_alerts"]}</span>
                <span class="stat-value stat-red">{alerts}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── 5) التذييل ──
        st.markdown(f"""
        <div class="footer">
            <div class="footer-title">🎯 ActionLens · 2026</div>
            <div class="footer-sub">{t["footer_sub"]}</div>
            <div class="footer-links">
                <a href="https://github.com" target="_blank">GitHub</a>
                <a href="https://linkedin.com" target="_blank">LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
