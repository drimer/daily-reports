import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from typing import Iterable

from src.report_senders.config import ReportSendersConfig


def send(reports: Iterable):
    subject = 'My daily report for {}'.format(datetime.today().strftime('%d-%m-%Y'))
    message = ('<br/>' * 2).join(str(report) for report in reports)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = ReportSendersConfig.FROM_EMAIL_ADDRESS
    msg['To'] = ReportSendersConfig.RECIPIENT_EMAIL_ADDRESS
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(ReportSendersConfig.FROM_EMAIL_ADDRESS, ReportSendersConfig.FROM_EMAIL_PASSWORD)
        smtp_server.sendmail(ReportSendersConfig.FROM_EMAIL_ADDRESS, ReportSendersConfig.RECIPIENT_EMAIL_ADDRESS, msg.as_string())
