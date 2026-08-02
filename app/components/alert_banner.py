# SafeWatch - app/components/alert_banner.py

import streamlit as st
from pathlib import Path


def render_alert_banner(label: str, confidence: float):
    """
    بتعرض بانر التنبيه الأحمر
    """
    st.error(f"""
    🚨 تم اكتشاف سلوك مشبوه!
    
    **النوع:** {label.upper()}  
    **الثقة:** {confidence:.2%}
    """)

    # صوت التنبيه
    audio_path = Path("app/assets/alert_sound.mp3")
    if audio_path.exists():
        st.audio(str(audio_path), autoplay=True)


def render_safe_banner():
    """
    بتعرض بانر الأمان الأخضر
    """
    st.success("✅ لا يوجد سلوك مشبوه")
