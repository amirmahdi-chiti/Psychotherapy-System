import smtplib
import pyotp
from email.message import EmailMessage

# Your email configuration
SMTP_SERVER = 'smtp.your_email_provider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def generate_otp(secret: str):
    totp = pyotp.TOTP(secret)
    return totp.now()

def send_otp_via_email(recipient_email: str, otp: str):
    msg = EmailMessage()
    msg.set_content(f"Your OTP code is: {otp}")
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def verify_otp(secret: str, otp: str):
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)
