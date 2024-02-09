import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from typing import Iterable

from src.report_senders.config import ReportSendersConfig


class EmailReportSender:
    def __init__(self, report_senders_config: ReportSendersConfig):
        self.config = report_senders_config

    def send(self, reports: Iterable):
        subject = 'My daily report for {}'.format(datetime.today().strftime('%d-%m-%Y'))
        message = ('<br/>' * 2).join(str(report) for report in reports)

        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = self.config.FROM_EMAIL_ADDRESS
        msg['To'] = self.config.RECIPIENT_EMAIL_ADDRESS
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(
                self.config.FROM_EMAIL_ADDRESS,
                self.config.FROM_EMAIL_PASSWORD
            )
            smtp_server.sendmail(
                self.config.FROM_EMAIL_ADDRESS,
                self.config.RECIPIENT_EMAIL_ADDRESS,
                msg.as_string(),
            )
