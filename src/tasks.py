import datetime

from src.email import send_email
from src.notion.models import Task, EmailReport


def notion_daily_report():
    tasks = (
        Task(title='Do laundry', due_by=datetime.datetime.today()),
        Task(title='Weekly grocery shopping', due_by=datetime.datetime.today()),
    )
    report = EmailReport(tasks)
    send_email(report.body())
