import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

class EmailService:
    """Service for sending emails"""
    
    async def send_confirmation_email(self, to_email: str, full_name: str, date: str, time: str):
        """Send interview confirmation email"""
        message = MIMEMultipart()
        message["From"] = settings.EMAIL_FROM
        message["To"] = to_email
        message["Subject"] = "Interview Confirmation"
        
        body = f"""
        Dear {full_name},
        
        Your interview has been scheduled for:
        Date: {date}
        Time: {time}
        
        Best regards,
        PalmMind Team
        """
        
        message.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
            server.send_message(message)