# SafeWatch - app/components/sidebar.py
import streamlit as st

def render_sidebar():
    with st.sidebar:

        # ── Brand ──
        st.markdown("""
            <div style='
                text-align: center;
                padding: 24px 0 8px;
            '>
                <div style='
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(135deg, #f0a500, #ffc93c);
                    border-radius: 50%;
                    width: 64px;
                    height: 64px;
                    font-size: 2rem;
                    box-shadow: 0 4px 16px rgba(240,165,0,0.35);
                    margin-bottom: 12px;
                '>🛡️</div>
                <h2 style='
                    color: #f0a500;
                    margin: 0;
                    font-size: 1.5rem;
                    letter-spacing: 1px;
                '>SafeWatch</h2>
                <p style='
                    color: #8a9bb5;
                    font-size: 0.75rem;
                    margin: 4px 0 0;
                '>نظام كشف السلوك المشبوه</p>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Navigation ──
        st.markdown("""
            <p style='
                color: #8a9bb5;
                font-size: 0.7rem;
                font-weight: 700;
                letter-spacing: 2px;
                margin: 0 0 8px;
                text-transform: uppercase;
            '>القائمة</p>
        """, unsafe_allow_html=True)

        st.page_link("app.py",               label="🏠  الرئيسية")
        st.page_link("pages/image_test.py",  label="🖼️  اختبار صورة")
        st.page_link("pages/live_camera.py", label="📹  كاميرا مباشرة")

        st.divider()

        # ── Settings ──
        st.markdown("""
            <p style='
                color: #8a9bb5;
                font-size: 0.7rem;
                font-weight: 700;
                letter-spacing: 2px;
                margin: 0 0 8px;
                text-transform: uppercase;
            '>الإعدادات</p>
        """, unsafe_allow_html=True)

        threshold = st.slider(
            "حد التنبيه",
            min_value=0.5,
            max_value=1.0,
            value=st.session_state.get("threshold", 0.75),
            step=0.05,
            format="%.0f%%"
        )
        st.session_state["threshold"] = threshold

        # مؤشر الحالة
        color  = "#e74c3c" if threshold >= 0.85 else "#f0a500" if threshold >= 0.70 else "#2ecc71"
        status = "حساسية عالية" if threshold >= 0.85 else "حساسية متوسطة" if threshold >= 0.70 else "حساسية منخفضة"
        st.markdown(f"""
            <div style='
                background: #0d1b2a;
                border-radius: 8px;
                padding: 8px 12px;
                margin-top: 6px;
                display: flex;
                align-items: center;
                gap: 8px;
            '>
                <span style='
                    width: 10px;
                    height: 10px;
                    border-radius: 50%;
                    background: {color};
                    display: inline-block;
                    box-shadow: 0 0 6px {color};
                '></span>
                <span style='color: {color}; font-size: 0.8rem; font-weight: 600;'>
                    {status}
                </span>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Stats ──
        st.markdown("""
            <p style='
                color: #8a9bb5;
                font-size: 0.7rem;
                font-weight: 700;
                letter-spacing: 2px;
                margin: 0 0 10px;
                text-transform: uppercase;
            '>إحصائيات الجلسة</p>
        """, unsafe_allow_html=True)

        predictions = st.session_state.get("total_predictions", 0)
        alerts      = st.session_state.get("total_alerts", 0)
        emails      = st.session_state.get("total_emails", 0)

        st.markdown(f"""
            <div style='display: flex; flex-direction: column; gap: 8px;'>
                <div style='
                    background: #0d1b2a;
                    border-radius: 10px;
                    padding: 10px 14px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                '>
                    <span style='color:#8a9bb5; font-size:0.82rem;'>🔍 تحليلات</span>
                    <span style='color:#f0a500; font-weight:700; font-size:1rem;'>{predictions}</span>
                </div>
                <div style='
                    background: #0d1b2a;
                    border-radius: 10px;
                    padding: 10px 14px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                '>
                    <span style='color:#8a9bb5; font-size:0.82rem;'>🚨 تنبيهات</span>
                    <span style='color:#e74c3c; font-weight:700; font-size:1rem;'>{alerts}</span>
                </div>
                <div style='
                    background: #0d1b2a;
                    border-radius: 10px;
                    padding: 10px 14px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                '>
                    <span style='color:#8a9bb5; font-size:0.82rem;'>📧 إيميلات</span>
                    <span style='color:#2ecc71; font-weight:700; font-size:1rem;'>{emails}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── Footer ──
        st.markdown("""
            <div style='text-align:center; padding: 4px 0 8px;'>
                <span style='color:#8a9bb5; font-size:0.72rem;'>
                    SafeWatch v1.0 — 2026
                </span>
            </div>
        """, unsafe_allow_html=True)
