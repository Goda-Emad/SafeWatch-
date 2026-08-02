# SafeWatch - app/components/stats_panel.py

import streamlit as st
import pandas as pd
from pathlib import Path


def render_stats_panel():
    """
    بتعرض إحصائيات الجلسة
    """
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔍 الصور المحللة",
            st.session_state.get("total_predictions", 0)
        )
    with col2:
        st.metric(
            "🚨 التنبيهات",
            st.session_state.get("total_alerts", 0)
        )
    with col3:
        st.metric(
            "📧 إيميلات مرسلة",
            st.session_state.get("total_emails", 0)
        )
    with col4:
        st.metric(
            "⚙️ حد التنبيه",
            f"{st.session_state.get('threshold', 0.75):.0%}"
        )


def render_alerts_log():
    """
    بتعرض سجل التنبيهات من CSV
    """
    log_path = Path("alerts/alerts_log.csv")

    if not log_path.exists():
        st.info("لا يوجد تنبيهات مسجلة حتى الآن")
        return

    df = pd.read_csv(log_path)

    if df.empty:
        st.info("السجل فاضي")
        return

    st.markdown("#### 📋 سجل التنبيهات")
    st.dataframe(
        df.sort_values("timestamp", ascending=False),
        use_container_width=True
    )

    # زرار تحميل السجل
    st.download_button(
        label="⬇️ تحميل السجل",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="alerts_log.csv",
        mime="text/csv"
    )
