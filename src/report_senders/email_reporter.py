import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from typing import Iterable


def send(reports: Iterable):
    subject = 'My daily report for {}'.format(datetime.today().strftime('%d-%m-%Y'))
    message = ('<br/>' * 2).join(str(report) for report in reports)

    recipient_email = os.environ['RECIPIENT_EMAIL_ADDRESS']
    from_email_address = os.environ['FROM_EMAIL_ADDRESS']
    from_email_password = os.environ['FROM_EMAIL_PASSWORD']

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_email_address
    msg['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(from_email_address, from_email_password)
        smtp_server.sendmail(from_email_address, recipient_email, msg.as_string())
    print("Message sent!")
