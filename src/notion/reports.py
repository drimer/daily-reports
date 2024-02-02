from src.core.reports import Report, ReportRunner
from src.notion.api_client import as_tasks, NotionApiClient
from src.notion.config import NotionConfig
from src.notion.models import EmailReport


class NotionReportRunner(ReportRunner):
    def __init__(self, notion_api_client: NotionApiClient):
        self.notion_api_client = notion_api_client

    def run(self) -> Report:
        notion_response = self.notion_api_client.get_todays_tasks()
        tasks = as_tasks(notion_response)

        return EmailReport(tasks)
