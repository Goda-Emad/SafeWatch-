# SafeWatch - app/components/prediction_card.py

import streamlit as st


def render_prediction_card(label: str, confidence: float, all_scores: dict):
    """
    بتعرض نتيجة التحليل
    """
    st.markdown("#### 🔍 نتيجة التحليل")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("السلوك المكتشف", label.upper())
    with col2:
        st.metric("نسبة الثقة", f"{confidence:.2%}")

    st.divider()

    st.markdown("#### 📊 كل السلوكيات")
    for lbl, score in sorted(
        all_scores.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        color = "🔴" if lbl == "fighting" else "🟢"
        st.progress(score, text=f"{color} {lbl}: {score:.2%}")
