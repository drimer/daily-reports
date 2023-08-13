from src.email import send_email
from src.notion.api_client import pull_db_entries_from_notion, as_task, TODAY_VIEW_FILTER, as_tasks
from src.notion.models import Task, EmailReport


def notion_daily_report():
    # tasks = (
    #     Task(title='Do laundry', due_by=datetime.datetime.today()),
    #     Task(title='Weekly grocery shopping', due_by=datetime.datetime.today()),
    # )
    database_id = '7f159b000c2e4365b1a0efec3e6e60a7'
    filters = TODAY_VIEW_FILTER
    notion_response = pull_db_entries_from_notion(database_id, filters)
    tasks = as_tasks(notion_response)

    report = EmailReport(tasks)
    send_email(report.body())
