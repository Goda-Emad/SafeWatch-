# SafeWatch - app/components/sidebar.py
import streamlit as st

# ============================================================
# الترجمة - Translation
# ============================================================
TRANSLATIONS = {
    "ar": {
        "brand_name": "SafeWatch",
        "brand_sub": "نظام المراقبة الذكي",
        "brand_icon": "🛡️",
        "nav_home": "🏠 الرئيسية",
        "nav_image": "📷 رفع صورة",
        "nav_camera": "🎥 كاميرا لايف",
        "nav_reports": "📊 التقارير",
        "nav_settings": "⚙️ الإعدادات",
        "dark_toggle": "☀️ فاتح",
        "light_toggle": "🌙 داكن",
        "lang_btn": "🌐 English",
        "nav_label": "القائمة الرئيسية",
        "footer_sub": "نظام مراقبة متطور بالذكاء الاصطناعي",
        "footer_rights": "جميع الحقوق محفوظة",
        "online": "🟢 متصل",
        "offline": "🔴 غير متصل",
    },
    "en": {
        "brand_name": "SafeWatch",
        "brand_sub": "Smart Monitoring System",
        "brand_icon": "🛡️",
        "nav_home": "🏠 Home",
        "nav_image": "📷 Upload Image",
        "nav_camera": "🎥 Live Camera",
        "nav_reports": "📊 Reports",
        "nav_settings": "⚙️ Settings",
        "dark_toggle": "☀️ Light",
        "light_toggle": "🌙 Dark",
        "lang_btn": "🌐 العربية",
        "nav_label": "MAIN MENU",
        "footer_sub": "Advanced AI-Powered Monitoring System",
        "footer_rights": "All Rights Reserved",
        "online": "🟢 Online",
        "offline": "🔴 Offline",
    },
}

# ============================================================
# تهيئة الجلسة - Session Initialization
# ============================================================
def _init_session():
    """تهيئة جميع متغيرات الجلسة"""
    defaults = {
        "lang": "ar",
        "dark_mode": True,
        "active_page": "home",
        "system_status": "online",
        "camera_count": 4,
        "detection_count": 0,
        "alert_count": 0,
        "user_name": "Admin",
        "last_update": None,
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ============================================================
# الدالة الرئيسية - Main Render Function
# ============================================================
def render_sidebar():
    """عرض الشريط الجانبي الاحترافي"""
    _init_session()

    dark = st.session_state["dark_mode"]
    lang = st.session_state["lang"]
    t = TRANSLATIONS[lang]

    # ── تحديد الألوان حسب الوضع (داكن / فاتح) ──
    if dark:
        # الألوان الداكنة
        BG = "#0a0e17"
        BG_SECONDARY = "#111827"
        BG_CARD = "#1a2234"
        BG_HOVER = "#243047"
        TEXT_PRIMARY = "#f0f4ff"
        TEXT_SECONDARY = "#94a3b8"
        TEXT_MUTED = "#64748b"
        BORDER = "#1e293b"
        BORDER_LIGHT = "#334155"
        GREEN = "#22d3ee"
        BLUE = "#60a5fa"
        RED = "#f87171"
        PURPLE = "#a78bfa"
        ORANGE = "#fb923c"
        BUTTON_BG = "#1e293b"
        BUTTON_HOVER = "#334155"
        SHADOW = "rgba(0, 0, 0, 0.4)"
        GRADIENT = "linear-gradient(135deg, #1a2234, #0a0e17)"
        STATUS_ONLINE = "#22d3ee"
        STATUS_OFFLINE = "#f87171"
    else:
        # الألوان الفاتحة
        BG = "#f0f4ff"
        BG_SECONDARY = "#ffffff"
        BG_CARD = "#f8fafc"
        BG_HOVER = "#e2e8f0"
        TEXT_PRIMARY = "#0f172a"
        TEXT_SECONDARY = "#475569"
        TEXT_MUTED = "#94a3b8"
        BORDER = "#e2e8f0"
        BORDER_LIGHT = "#cbd5e1"
        GREEN = "#0ea5e9"
        BLUE = "#3b82f6"
        RED = "#ef4444"
        PURPLE = "#8b5cf6"
        ORANGE = "#f59e0b"
        BUTTON_BG = "#f1f5f9"
        BUTTON_HOVER = "#e2e8f0"
        SHADOW = "rgba(0, 0, 0, 0.08)"
        GRADIENT = "linear-gradient(135deg, #ffffff, #f0f4ff)"
        STATUS_ONLINE = "#22c55e"
        STATUS_OFFLINE = "#ef4444"

    # ── جلب بيانات الجلسة ──
    page = st.session_state.get("active_page", "home")
    status = st.session_state.get("system_status", "online")
    cameras = st.session_state.get("camera_count", 0)
    detections = st.session_state.get("detection_count", 0)
    alerts = st.session_state.get("alert_count", 0)
    user = st.session_state.get("user_name", "Admin")

    status_text = t["online"] if status == "online" else t["offline"]
    status_color = STATUS_ONLINE if status == "online" else STATUS_OFFLINE
    status_dot = "🟢" if status == "online" else "🔴"

    # ── CSS المتقدم ──
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');

    /* ===== أساسيات الـ Sidebar ===== */
    [data-testid="stSidebar"] {{
        background: {BG} !important;
        border-right: 1px solid {BORDER} !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background: {BG} !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebarNav"] {{
        display: none !important;
    }}
    
    /* ===== إزالة المسافات ===== */
    [data-testid="stSidebar"] section[data-testid="stSidebarContent"] {{
        padding: 0.75rem 0.75rem 1.5rem 0.75rem !important;
    }}
    [data-testid="stSidebar"] .block-container {{
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stMarkdown {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    
    /* ===== الخطوط ===== */
    [data-testid="stSidebar"] * {{
        font-family: 'Inter', 'Cairo', -apple-system, sans-serif !important;
    }}
    
    /* ===== الأزرار الرئيسية ===== */
    [data-testid="stSidebar"] .stButton {{
        margin: 0 0 4px 0 !important;
        padding: 0 !important;
    }}
    [data-testid="stSidebar"] .stButton > button {{
        background: {BUTTON_BG} !important;
        color: {TEXT_SECONDARY} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 10px !important;
        width: 100% !important;
        padding: 0.65rem 1rem !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        text-align: left !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 1px 2px {SHADOW} !important;
        height: auto !important;
        line-height: 1.5 !important;
        white-space: normal !important;
        gap: 10px !important;
        display: flex !important;
        align-items: center !important;
        letter-spacing: 0.3px !important;
    }}
    [data-testid="stSidebar"] .stButton > button:hover {{
        background: {BG_HOVER} !important;
        border-color: {GREEN} !important;
        color: {TEXT_PRIMARY} !important;
        transform: translateX(4px) !important;
        box-shadow: 0 4px 12px rgba(34, 211, 238, 0.15) !important;
    }}
    [data-testid="stSidebar"] .stButton > button:active {{
        transform: translateX(2px) !important;
    }}
    
    /* ===== الزر النشط ===== */
    .nav-active .stButton > button {{
        background: {BG_CARD} !important;
        color: {GREEN} !important;
        border: 1px solid {GREEN} !important;
        border-left: 4px solid {GREEN} !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 16px rgba(34, 211, 238, 0.2) !important;
    }}
    .nav-active .stButton > button:hover {{
        transform: translateX(4px) !important;
    }}
    
    /* ===== أزرار التبديل الصغيرة ===== */
    .toggle-btn .stButton > button {{
        font-size: 0.72rem !important;
        padding: 0.35rem 0.5rem !important;
        border-radius: 8px !important;
        text-align: center !important;
        justify-content: center !important;
        display: flex !important;
        background: {BG_CARD} !important;
        border-color: {BORDER} !important;
    }}
    .toggle-btn .stButton {{
        margin-bottom: 0 !important;
    }}
    .toggle-btn .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px {SHADOW} !important;
    }}
    
    /* ===== الأعمدة ===== */
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {{
        gap: 6px !important;
        margin: 0 0 6px 0 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] > div {{
        padding: 0 !important;
        flex: 1 !important;
    }}
    
    /* ===== خلفية التطبيق ===== */
    .stApp {{
        background: {BG_SECONDARY} !important;
    }}
    
    /* ===== العلامة التجارية ===== */
    .brand-container {{
        padding: 2px 0 6px 0;
    }}
    .brand {{
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 12px 4px 14px 4px;
        background: {GRADIENT};
        border-radius: 12px;
        padding: 12px 16px;
        border: 1px solid {BORDER};
        transition: all 0.3s ease;
    }}
    .brand:hover {{
        border-color: {GREEN};
        box-shadow: 0 4px 20px rgba(34, 211, 238, 0.1);
    }}
    .brand-icon {{
        font-size: 2.4rem;
        line-height: 1;
        filter: drop-shadow(0 2px 8px rgba(34, 211, 238, 0.2));
        animation: pulse 2s ease-in-out infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    .brand-title {{
        font-size: 1.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, {GREEN}, {BLUE});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }}
    .brand-sub {{
        font-size: 0.6rem;
        color: {TEXT_SECONDARY};
        letter-spacing: 1.8px;
        text-transform: uppercase;
        margin-top: 2px;
        font-weight: 600;
    }}
    
    /* ===== تسميات الأقسام ===== */
    .section-label {{
        font-size: 0.58rem;
        color: {TEXT_MUTED};
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin: 1.2rem 0 0.6rem 0.2rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .section-label::after {{
        content: '';
        flex: 1;
        height: 1px;
        background: {BORDER};
    }}
    
    /* ===== الفاصل ===== */
    .divider {{
        height: 1px;
        background: {BORDER};
        margin: 0.5rem 0;
    }}
    .divider-glow {{
        height: 2px;
        background: linear-gradient(90deg, transparent, {GREEN}, transparent);
        margin: 0.8rem 0;
        opacity: 0.3;
        border-radius: 2px;
    }}
    
    /* ===== بطاقة الحالة ===== */
    .status-card {{
        background: {BG_CARD};
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 0.75rem 1rem;
        margin: 0.8rem 0 0.2rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s ease;
    }}
    .status-card:hover {{
        border-color: {status_color};
        box-shadow: 0 4px 16px rgba(34, 211, 238, 0.08);
    }}
    .status-label {{
        color: {TEXT_SECONDARY};
        font-size: 0.78rem;
        font-weight: 500;
    }}
    .status-value {{
        color: {status_color};
        font-size: 0.8rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .status-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: {status_color};
        display: inline-block;
        animation: blink 1.5s ease-in-out infinite;
    }}
    @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.3; }}
    }}
    
    /* ===== بطاقات الإحصائيات المصغرة ===== */
    .stats-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 4px;
        margin: 8px 0 4px 0;
    }}
    .stat-mini {{
        background: {BG_CARD};
        border: 1px solid {BORDER};
        border-radius: 8px;
        padding: 0.5rem 0.3rem;
        text-align: center;
        transition: all 0.3s ease;
    }}
    .stat-mini:hover {{
        border-color: {GREEN};
        transform: translateY(-2px);
        box-shadow: 0 4px 12px {SHADOW};
    }}
    .stat-mini-number {{
        font-size: 1.1rem;
        font-weight: 800;
        color: {TEXT_PRIMARY};
        display: block;
        line-height: 1.2;
    }}
    .stat-mini-number.green {{ color: {GREEN}; }}
    .stat-mini-number.blue {{ color: {BLUE}; }}
    .stat-mini-number.red {{ color: {RED}; }}
    .stat-mini-number.purple {{ color: {PURPLE}; }}
    .stat-mini-label {{
        font-size: 0.5rem;
        color: {TEXT_MUTED};
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
        display: block;
        margin-top: 2px;
    }}
    
    /* ===== التذييل ===== */
    .footer {{
        text-align: center;
        margin-top: 1.2rem;
        padding-top: 0.8rem;
        border-top: 1px solid {BORDER};
    }}
    .footer-title {{
        font-size: 0.75rem;
        color: {TEXT_SECONDARY};
        font-weight: 600;
        margin-bottom: 3px;
    }}
    .footer-title span {{
        background: linear-gradient(135deg, {GREEN}, {BLUE});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    .footer-sub {{
        font-size: 0.58rem;
        color: {TEXT_MUTED};
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }}
    .footer-rights {{
        font-size: 0.5rem;
        color: {TEXT_MUTED};
        opacity: 0.6;
        margin-bottom: 6px;
    }}
    .footer-links {{
        margin-top: 6px;
        display: flex;
        justify-content: center;
        gap: 14px;
    }}
    .footer-links a {{
        color: {TEXT_SECONDARY};
        text-decoration: none;
        font-size: 0.68rem;
        font-weight: 600;
        transition: all 0.3s ease;
        padding: 4px 10px;
        border-radius: 6px;
        background: {BG_CARD};
        border: 1px solid {BORDER};
    }}
    .footer-links a:hover {{
        color: {GREEN};
        border-color: {GREEN};
        transform: translateY(-2px);
        box-shadow: 0 4px 12px {SHADOW};
    }}
    
    /* ===== مستخدم ===== */
    .user-info {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 12px;
        background: {BG_CARD};
        border-radius: 10px;
        border: 1px solid {BORDER};
        margin: 6px 0 2px 0;
    }}
    .user-avatar {{
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: linear-gradient(135deg, {GREEN}, {BLUE});
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        font-weight: 800;
        color: {BG};
        flex-shrink: 0;
    }}
    .user-name {{
        font-size: 0.78rem;
        font-weight: 600;
        color: {TEXT_PRIMARY};
    }}
    .user-role {{
        font-size: 0.55rem;
        color: {TEXT_MUTED};
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ── عرض المحتوى ──
    with st.sidebar:

        # ── 1) أزرار التبديل ──
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

        # ── 2) العلامة التجارية ──
        st.markdown(f"""
        <div class="brand-container">
            <div class="brand">
                <div class="brand-icon">{t["brand_icon"]}</div>
                <div>
                    <div class="brand-title">{t["brand_name"]}</div>
                    <div class="brand-sub">{t["brand_sub"]}</div>
                </div>
            </div>
            <div class="divider-glow"></div>
            <div class="section-label">{t["nav_label"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── 3) أزرار التنقل ──
        nav_items = {
            "home": {"label": t["nav_home"], "target": "app.py", "icon": "🏠"},
            "image": {"label": t["nav_image"], "target": "pages/image_test.py", "icon": "📷"},
            "camera": {"label": t["nav_camera"], "target": "pages/live_camera.py", "icon": "🎥"},
            "reports": {"label": t["nav_reports"], "target": "pages/reports.py", "icon": "📊"},
            "settings": {"label": t["nav_settings"], "target": "pages/settings.py", "icon": "⚙️"},
        }

        for key, item in nav_items.items():
            is_active = (page == key)
            if is_active:
                st.markdown('<div class="nav-active">', unsafe_allow_html=True)
            
            # إضافة الأيقونة قبل النص
            button_label = item["label"]
            if st.button(button_label, key=f"nav_{key}", use_container_width=True):
                st.session_state["active_page"] = key
                try:
                    st.switch_page(item["target"])
                except Exception:
                    st.error(f"⚠️ صفحة {item['target']} غير موجودة")
            
            if is_active:
                st.markdown('</div>', unsafe_allow_html=True)

        # ── 4) معلومات المستخدم ──
        st.markdown(f"""
        <div class="user-info">
            <div class="user-avatar">{user[0].upper()}</div>
            <div>
                <div class="user-name">{user}</div>
                <div class="user-role">Administrator</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── 5) حالة النظام ──
        st.markdown(f"""
        <div class="status-card">
            <span class="status-label">🔹 حالة النظام</span>
            <span class="status-value">
                <span class="status-dot"></span>
                {status_text}
            </span>
        </div>
        """, unsafe_allow_html=True)

        # ── 6) إحصائيات سريعة ──
        st.markdown("""
        <div class="stats-grid">
            <div class="stat-mini">
                <span class="stat-mini-number green">{}</span>
                <span class="stat-mini-label">كاميرات</span>
            </div>
            <div class="stat-mini">
                <span class="stat-mini-number blue">{}</span>
                <span class="stat-mini-label">اكتشافات</span>
            </div>
            <div class="stat-mini">
                <span class="stat-mini-number red">{}</span>
                <span class="stat-mini-label">تنبيهات</span>
            </div>
        </div>
        """.format(cameras, detections, alerts), unsafe_allow_html=True)

        # ── 7) التذييل ──
        st.markdown(f"""
        <div class="footer">
            <div class="footer-title">🛡️ <span>{t["brand_name"]}</span> · 2026</div>
            <div class="footer-sub">{t["footer_sub"]}</div>
            <div class="footer-rights">© 2026 {t["footer_rights"]}</div>
            <div class="footer-links">
                <a href="https://github.com" target="_blank">GitHub</a>
                <a href="https://linkedin.com" target="_blank">LinkedIn</a>
                <a href="#" target="_blank">Docs</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
