# SafeWatch - app/components/sidebar.py
import streamlit as st

# ═══════════════════════════════════════
# Translations
# ═══════════════════════════════════════
TRANSLATIONS = {
    "ar": {
        "brand_sub":      "نظام المراقبة الذكي",
        "menu_label":     "القائمة",
        "nav_home":       "🏠  الرئيسية",
        "nav_image":      "🖼️  اختبار صورة",
        "nav_camera":     "📹  كاميرا مباشرة",
        "stats_label":    "إحصائيات الجلسة",
        "stat_analysis":  "🔍 تحليلات",
        "stat_alerts":    "🚨 تنبيهات",
        "stat_emails":    "📧 إيميلات",
        "settings_label": "الإعدادات",
        "dark_mode":      "🌙 الوضع الداكن",
        "light_mode":     "☀️ الوضع الفاتح",
        "lang_toggle":    "🌐 English",
        "footer":         "نظام المراقبة الذكي",
    },
    "en": {
        "brand_sub":      "Smart Surveillance System",
        "menu_label":     "MENU",
        "nav_home":       "🏠  Home",
        "nav_image":      "🖼️  Image Test",
        "nav_camera":     "📹  Live Camera",
        "stats_label":    "SESSION STATS",
        "stat_analysis":  "🔍 Analyses",
        "stat_alerts":    "🚨 Alerts",
        "stat_emails":    "📧 Emails",
        "settings_label": "SETTINGS",
        "dark_mode":      "🌙 Dark Mode",
        "light_mode":     "☀️ Light Mode",
        "lang_toggle":    "🌐 العربية",
        "footer":         "Smart Surveillance System",
    },
}


def _init_session():
    """Initialize session state defaults."""
    if "lang" not in st.session_state:
        st.session_state["lang"] = "ar"
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = False


def _get_theme_colors(dark: bool):
    if dark:
        return {
            "NAVY":   "#0d1b2a",
            "GOLD":   "#f0a500",
            "BORDER": "#1e2e42",
            "WHITE":  "#e8edf5",
            "GREY":   "#8a9bb5",
            "DARK":   "#060f1a",
            "CARD_BG":"#0d1b2a",
            "BG":     "#060f1a",
        }
    else:
        return {
            "NAVY":   "#1a2744",
            "GOLD":   "#f0a500",
            "BORDER": "#2a3a55",
            "WHITE":  "#e8edf5",
            "GREY":   "#8a9bb5",
            "DARK":   "#0d1b2a",
            "CARD_BG":"#0d1b2a",
            "BG":     "#0d1b2a",
        }


def render_sidebar():
    _init_session()

    dark = st.session_state["dark_mode"]
    lang = st.session_state["lang"]
    t    = TRANSLATIONS[lang]
    c    = _get_theme_colors(dark)

    # ─── Dynamic CSS ───────────────────────────────────────────
    st.markdown(
        "<style>"
        "@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');"

        # Sidebar background
        f"[data-testid='stSidebar']{{background:linear-gradient(180deg,{c['NAVY']} 0%,{c['DARK']} 100%)!important;"
        f"border-right:2px solid {c['GOLD']}!important;}}"
        "[data-testid='stSidebarNav']{display:none!important;}"

        # Text colour inside sidebar
        f"[data-testid='stSidebar'] div,[data-testid='stSidebar'] span,"
        f"[data-testid='stSidebar'] p,[data-testid='stSidebar'] label{{color:{c['WHITE']}!important;"
        f"font-family:'Cairo',sans-serif!important;}}"

        # Nav buttons base
        "[data-testid='stSidebar'] .stButton>button{"
        f"background:transparent!important;border:1px solid {c['BORDER']}!important;"
        f"color:{c['GREY']}!important;border-radius:10px!important;"
        "width:100%!important;font-size:.88rem!important;font-weight:600!important;"
        "padding:10px 14px!important;margin-bottom:4px!important;transition:all .18s!important;"
        "text-align:right!important;}"
        "[data-testid='stSidebar'] .stButton>button:hover{"
        f"background:{c['GOLD']}22!important;color:{c['GOLD']}!important;border-color:{c['GOLD']}66!important;}}"

        # Active home button
        f".home-btn .stButton>button{{background:{c['GOLD']}18!important;"
        f"border:1px solid {c['GOLD']}55!important;color:{c['GOLD']}!important;font-weight:700!important;}}"
        f".home-btn .stButton>button:hover{{background:{c['GOLD']}35!important;border-color:{c['GOLD']}!important;}}"

        # Toggle buttons (dark/lang)
        f".toggle-btn .stButton>button{{background:{c['DARK']}!important;"
        f"border:1px solid {c['BORDER']}!important;color:{c['WHITE']}!important;"
        f"font-size:.82rem!important;padding:8px 12px!important;border-radius:20px!important;"
        f"font-weight:600!important;}}"
        f".toggle-btn .stButton>button:hover{{border-color:{c['GOLD']}!important;color:{c['GOLD']}!important;}}"

        # Main app background (dark mode only)
        + (
            ".stApp{background:#060f1a!important;}"
            ".stApp .stMarkdown h1,.stApp .stMarkdown h2,.stApp .stMarkdown h3{color:#e8edf5!important;}"
            ".stApp [data-testid='stMetricLabel']{color:#8a9bb5!important;}"
            ".stApp [data-testid='stMetricValue']{color:#f0a500!important;}"
            if dark else
            ".stApp{background:#f0f4f8!important;}"
        )
        + "</style>",
        unsafe_allow_html=True,
    )

    with st.sidebar:

        # ── Brand ───────────────────────────────────────────────
        st.markdown(
            f'<div style="text-align:center;padding:24px 0 16px;">'
            f'<div style="display:inline-flex;align-items:center;justify-content:center;'
            f'background:linear-gradient(135deg,{c["GOLD"]},{c["NAVY"]});'
            f'border-radius:50%;width:68px;height:68px;font-size:2.2rem;'
            f'box-shadow:0 4px 18px rgba(240,165,0,0.35);margin-bottom:12px;">🛡️</div>'
            f'<div style="font-size:1.4rem;font-weight:700;color:{c["GOLD"]};letter-spacing:1px;">SafeWatch</div>'
            f'<div style="font-size:0.7rem;color:{c["GREY"]};letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;">'
            f'{t["brand_sub"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(f'<div style="height:1px;background:{c["BORDER"]};margin-bottom:14px;"></div>', unsafe_allow_html=True)

        # ── Navigation ──────────────────────────────────────────
        st.markdown(
            f'<div style="font-size:0.68rem;color:{c["GREY"]};font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;padding:0 4px;margin-bottom:8px;">'
            f'{t["menu_label"]}</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="home-btn">', unsafe_allow_html=True)
        if st.button(t["nav_home"], key="nav_home", use_container_width=True):
            st.switch_page("app.py")
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button(t["nav_image"], key="nav_image", use_container_width=True):
            st.switch_page("pages/image_test.py")

        if st.button(t["nav_camera"], key="nav_camera", use_container_width=True):
            st.switch_page("pages/live_camera.py")

        st.markdown(f'<div style="height:1px;background:{c["BORDER"]};margin:14px 0;"></div>', unsafe_allow_html=True)

        # ── Stats ───────────────────────────────────────────────
        st.markdown(
            f'<div style="font-size:0.68rem;color:{c["GREY"]};font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;padding:0 4px;margin-bottom:10px;">'
            f'{t["stats_label"]}</div>',
            unsafe_allow_html=True,
        )

        predictions = st.session_state.get("total_predictions", 0)
        alerts      = st.session_state.get("total_alerts", 0)
        emails      = st.session_state.get("total_emails", 0)

        st.markdown(
            f'<div style="display:flex;flex-direction:column;gap:8px;">'

            f'<div style="background:{c["DARK"]};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {c["BORDER"]};">'
            f'<span style="color:{c["GREY"]};font-size:0.82rem;">{t["stat_analysis"]}</span>'
            f'<span style="color:{c["GOLD"]};font-weight:700;font-size:1rem;">{predictions}</span></div>'

            f'<div style="background:{c["DARK"]};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {c["BORDER"]};">'
            f'<span style="color:{c["GREY"]};font-size:0.82rem;">{t["stat_alerts"]}</span>'
            f'<span style="color:#e74c3c;font-weight:700;font-size:1rem;">{alerts}</span></div>'

            f'<div style="background:{c["DARK"]};border-radius:10px;padding:10px 14px;'
            f'display:flex;justify-content:space-between;align-items:center;'
            f'border:1px solid {c["BORDER"]};">'
            f'<span style="color:{c["GREY"]};font-size:0.82rem;">{t["stat_emails"]}</span>'
            f'<span style="color:#2ecc71;font-weight:700;font-size:1rem;">{emails}</span></div>'

            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(f'<div style="height:1px;background:{c["BORDER"]};margin:14px 0;"></div>', unsafe_allow_html=True)

        # ── Settings: Dark Mode + Language ──────────────────────
        st.markdown(
            f'<div style="font-size:0.68rem;color:{c["GREY"]};font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;padding:0 4px;margin-bottom:10px;">'
            f'{t["settings_label"]}</div>',
            unsafe_allow_html=True,
        )

        col_dark, col_lang = st.columns(2)

        with col_dark:
            st.markdown('<div class="toggle-btn">', unsafe_allow_html=True)
            dark_label = t["light_mode"] if dark else t["dark_mode"]
            if st.button(dark_label, key="toggle_dark", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with col_lang:
            st.markdown('<div class="toggle-btn">', unsafe_allow_html=True)
            if st.button(t["lang_toggle"], key="toggle_lang", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'<div style="height:1px;background:{c["BORDER"]};margin:14px 0 8px;"></div>', unsafe_allow_html=True)

        # ── Footer ───────────────────────────────────────────────
        st.markdown(
            f'<div style="font-size:0.68rem;color:{c["GREY"]};text-align:center;padding:0 2px;line-height:2;">'
            f'🛡️ SafeWatch v1.0 — 2026<br>'
            f'{t["footer"]}'
            f'</div>',
            unsafe_allow_html=True,
        )
