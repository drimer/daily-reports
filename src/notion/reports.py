from src.notion.api_client import as_tasks, NotionApiClient
from src.notion.config import NotionConfig
from src.notion.models import EmailReport


def build_daily_report():
    notion_response = NotionApiClient(NotionConfig.NOTION_API_TOKEN, NotionConfig.NOTION_TASKS_DB_ID).get_todays_tasks()
    tasks = as_tasks(notion_response)

    return EmailReport(tasks)
