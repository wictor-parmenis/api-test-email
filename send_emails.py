import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_email(toaddr, content, subject):
    fromaddr = "wictorsong@gmail.com"

    msg = MIMEMultipart()

    msg["From"] = fromaddr

    msg["To"] = toaddr

    msg["Subject"] = subject

    body = content

    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, os.getenv("password"))

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()


def send_multiple_emails(emails, content, subject):
    response = ''

    for email in emails:
        try:
            send_email(email, content, subject)
            response = {"message": "all emails sended with sucess.", "type": "sucess", "status": 200}
        except Exception as e:
            print(e, 'error')
            response = {"message": "failed in sending emails.", "status": 400, "type": "error"}

    return response