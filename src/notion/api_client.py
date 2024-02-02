from datetime import datetime

import requests
from src.notion.config import NotionConfig

from src.notion.models import Task

TODAY_VIEW_FILTER = {
    "filter": {
        "and": [
            {
                "property": "Kanban - State",
                "status": {
                    "is_not_empty": True
                }
            },
            {
                "property": "Kanban - State",
                "status": {
                    "does_not_equal": "Done",
                }
            },
            {
                "property": "Done",
                "checkbox": {
                    "does_not_equal": True,
                }
            },
            {
                "property": "Due",
                "date": {
                    "on_or_before": datetime.now().isoformat(),
                }
            },
        ]
    },
    "sorts": [
        {
            "property": "Due",
            "direction": "ascending",
        },
        {
            "property": "State",
            "direction": "descending",
        }
    ]
}


class NotionApiClient:
    def __init__(self, notion_config: NotionConfig):
        self.api_token = notion_config.NOTION_API_TOKEN
        self.db_id = notion_config.NOTION_TASKS_DB_ID

    def get_request_headers(self):
        return {
            "Authorization": "Bearer " + self.api_token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def get_entries_from_db(self, database_id: str, filters: dict):
        read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
        res = requests.request("POST", read_url, headers=self.get_request_headers(), json=filters)
        data = res.json()

        return data

    def get_todays_tasks(self):
        return self.get_entries_from_db(self.db_id, TODAY_VIEW_FILTER)


def as_task(api_json_response: dict) -> Task:
    if api_json_response['properties']['Due']['date']:
        due_by = api_json_response['properties']['Due']['date']['start']
    else:
        due_by = None

    return Task(
        title=api_json_response['properties']['Task']['title'][0]['text']['content'],
        due_by=due_by,
    )


def as_tasks(api_json_response: dict) -> list[Task]:
    return [as_task(json) for json in api_json_response['results']]
