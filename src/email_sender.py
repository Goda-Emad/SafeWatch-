# SafeWatch - src/email_sender.py

import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ═══════════════════════════════════════
# Gmail Config
# ═══════════════════════════════════════
def get_credentials():
    try:
        import streamlit as st
        sender   = st.secrets["GMAIL_USER"]
        password = st.secrets["GMAIL_APP_PASSWORD"]
        receiver = st.secrets["RECEIVER_EMAIL"]
    except Exception:
        sender   = os.getenv("GMAIL_USER")
        password = os.getenv("GMAIL_APP_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL")
    return sender, password, receiver


# ═══════════════════════════════════════
# تحميل قالب الإيميل
# ═══════════════════════════════════════
def load_template(label: str, confidence: float, timestamp: str) -> tuple:
    html_path = ROOT / "alerts" / "email_templates" / "alert_template.html"
    txt_path  = ROOT / "alerts" / "email_templates" / "alert_template.txt"

    placeholders = {
        "{LABEL}":          label.upper(),
        "{CONFIDENCE}":     f"{confidence:.2%}",
        "{CONFIDENCE_PCT}": str(int(confidence * 100)),
        "{TIMESTAMP}":      timestamp,
    }

    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        for k, v in placeholders.items():
            html = html.replace(k, v)
    else:
        html = f"""
        <h2>⚠️ SafeWatch Alert</h2>
        <p><b>السلوك:</b> {label.upper()}</p>
        <p><b>الثقة:</b> {confidence:.2%}</p>
        <p><b>الوقت:</b> {timestamp}</p>
        """

    if txt_path.exists():
        txt = txt_path.read_text(encoding="utf-8")
        for k, v in placeholders.items():
            txt = txt.replace(k, v)
    else:
        txt = (
            f"SafeWatch Alert\n"
            f"السلوك: {label.upper()}\n"
            f"الثقة: {confidence:.2%}\n"
            f"الوقت: {timestamp}"
        )

    return html, txt


# ═══════════════════════════════════════
# إرسال الإيميل
# ═══════════════════════════════════════
def send_alert_email(
    label: str,
    confidence: float,
    image_path: str = None
) -> bool:
    try:
        sender, password, receiver = get_credentials()

        if not all([sender, password, receiver]):
            print("❌ Gmail credentials ناقصة!")
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_body, txt_body = load_template(label, confidence, timestamp)

        # ── بناء الإيميل — mixed يحتوي alternative + attachment ──
        msg = MIMEMultipart("mixed")
        msg["Subject"] = f"🚨 SafeWatch Alert — {label.upper()} Detected"
        msg["From"]    = sender
        msg["To"]      = receiver

        # alternative جوه mixed عشان HTML يظهر صح
        alternative = MIMEMultipart("alternative")
        alternative.attach(MIMEText(txt_body,  "plain", "utf-8"))
        alternative.attach(MIMEText(html_body, "html",  "utf-8"))
        msg.attach(alternative)

        # إرفاق الصورة
        if image_path and Path(image_path).exists():
            with open(image_path, "rb") as img_file:
                image_attachment = MIMEImage(img_file.read())
                image_attachment.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=Path(image_path).name
                )
                msg.attach(image_attachment)

        # ── إرسال ──
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())

        print(f"✅ إيميل اتبعت لـ {receiver}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ خطأ في الـ Gmail credentials — تأكد من App Password")
        return False

    except smtplib.SMTPException as e:
        print(f"❌ خطأ في الإرسال: {e}")
        return False

    except Exception as e:
        print(f"❌ خطأ غير متوقع: {e}")
        return False
