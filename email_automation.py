import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "nikhilbathini47@gmail.com"
EMAIL_PASSWORD = "Sunny@1997"

def send_followup_email(recipient_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email

        server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
