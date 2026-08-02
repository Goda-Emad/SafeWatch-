# ActionLens - app/components/sidebar.py (حل بديل)
import streamlit as st

TRANSLATIONS = {
    # ... (نفس الترجمات)
}

def render_sidebar():
    _init_session()
    
    dark = st.session_state["dark_mode"]
    lang = st.session_state["lang"]
    t = TRANSLATIONS[lang]
    
    # CSS لتنسيق الأزرار والبطاقات
    st.markdown("""
    <style>
        /* كل الـ CSS اللي كنت بتستخدمه */
        .custom-sidebar { padding: 12px; }
        .stat-card { 
            background: #111622;
            border: 1px solid #1e2535;
            border-radius: 10px;
            padding: 10px 13px;
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
        }
        /* ... باقي التنسيقات */
    </style>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        # استخدام st.button العادية مع CSS
        col1, col2 = st.columns(2)
        with col1:
            if st.button(t["dark_toggle"] if dark else t["light_toggle"], key="dark_toggle", use_container_width=True):
                st.session_state["dark_mode"] = not dark
                st.rerun()
        with col2:
            if st.button(t["lang_btn"], key="lang_toggle", use_container_width=True):
                st.session_state["lang"] = "en" if lang == "ar" else "ar"
                st.rerun()
        
        # Brand (HTML)
        st.markdown(f"""
        <div style="padding:10px 0;">
            <div style="display:flex;align-items:center;gap:12px;">
                <div style="font-size:2rem;">🎯</div>
                <div>
                    <div style="font-size:1.2rem;font-weight:bold;">ActionLens</div>
                    <div style="font-size:0.7rem;color:#666;">{t["brand_sub"]}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation
        pages = {
            "home": ("🏠 الرئيسية", "app.py"),
            "image": ("🖼️ رفع صورة", "pages/image_test.py"),
            "camera": ("📹 كاميرا لايف", "pages/live_camera.py")
        }
        
        for key, (label, target) in pages.items():
            is_active = st.session_state.get("active_page") == key
            btn_class = "active" if is_active else ""
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state["active_page"] = key
                st.switch_page(target)
        
        # Stats (HTML)
        analyses = st.session_state.get("total_predictions", 0)
        actions = st.session_state.get("top_action", "—")
        alerts = st.session_state.get("total_alerts", 0)
        
        st.markdown(f"""
        <div style="margin-top:15px;">
            <div style="font-size:0.7rem;color:#666;text-transform:uppercase;margin-bottom:8px;">📊 {t["stats_label"]}</div>
            
            <div class="stat-card">
                <span>{t["stat_analyses"]}</span>
                <span style="color:#63d28c;font-weight:bold;">{analyses}</span>
            </div>
            <div class="stat-card">
                <span>{t["stat_actions"]}</span>
                <span style="color:#4f8ef7;font-weight:bold;">{actions}</span>
            </div>
            <div class="stat-card">
                <span>{t["stat_alerts"]}</span>
                <span style="color:#e74c3c;font-weight:bold;">{alerts}</span>
            </div>
            
            <div style="text-align:center;margin-top:20px;font-size:0.7rem;color:#666;">
                <div>🎯 ActionLens · 2026</div>
                <div style="font-size:0.6rem;margin-top:3px;">{t["footer_sub"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
