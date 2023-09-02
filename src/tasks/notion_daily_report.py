from datetime import datetime

from src.notion.api_client import pull_db_entries_from_notion, TODAY_VIEW_FILTER, as_tasks
from src.notion.models import EmailReport
from src.reporters.email_reporter import EmailReporter


def task():
    database_id = '7f159b000c2e4365b1a0efec3e6e60a7'
    filters = TODAY_VIEW_FILTER
    notion_response = pull_db_entries_from_notion(database_id, filters)
    tasks = as_tasks(notion_response)

    report = EmailReport(tasks)
    EmailReporter().send('My tasks for {}'.format(datetime.today().strftime('%d-%m-%Y')), report.body())


if __name__ == '__main__':
    task()
