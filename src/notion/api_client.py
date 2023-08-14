import requests
import os
from datetime import datetime

from src.notion.models import Task

TODAY_VIEW_FILTER = {
    "filter": {
        "and": [
            {
                "property": "Kanban - State",
                "select": {
                    "is_not_empty": True
                }
            },
            {
                "property": "Kanban - State",
                "select": {
                    "does_not_equal": "Done",
                }
            },
            {
                "property": "Priority",
                "select": {
                    "is_not_empty": True
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
            "property": "Priority",
            "direction": "descending"
        },
        {
            "property": "Due",
            "direction": "ascending",
        },
        {
            "property": "Recur interval (Days)",
            "direction": "descending",
        }
    ]
}


def get_request_headers():
    return {
        "Authorization": "Bearer " + os.environ['NOTION_API_TOKEN'],
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }


def pull_db_entries_from_notion(database_id: str, filters: dict):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", read_url, headers=get_request_headers(), json=filters)
    data = res.json()
    print(res.status_code)

    return data


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
