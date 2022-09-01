import smtplib
import logging
from email.message import EmailMessage

from settings import get_settings

app_settings = get_settings()
logging.getLogger(__name__)


def send_email_notification(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        server.starttls()
        server.login(app_settings.mail_login, app_settings.mail_password)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = 'Scraping notification'
        msg['From'] = app_settings.mail_login
        msg['To'] = app_settings.notification_email
        server.send_message(msg)
    except Exception as e:
        logging.error(e)
    finally:
        server.quit()
