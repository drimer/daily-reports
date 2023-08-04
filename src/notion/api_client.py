import requests
import os

from src.notion.models import Task

token = os.environ['NOTION_API_TOKEN']
DEFAULT_HEADERS = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


EXAMPLE_FILTER = {
  "filter": {
    "and": [
      {
        "property": "Kanban - State",
        "select": {
            "is_not_empty": True
        }
      },
      {
        "property": "Priority",
        "select": {
          "is_not_empty": True
        }
      }
    ]
  },
  "sorts": [
    {
      "property": "Priority",
      "direction": "descending"
    }
  ]
}


def pull_db_entries_from_notion(database_id: str, filters: dict):
    '''

    :param database_id:
    :param filters:
    :return:
    '''
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", read_url, headers=DEFAULT_HEADERS, json=filters)
    data = res.json()
    print(res.status_code)

    return data


def as_task(api_json_response: dict) -> Task:
    if api_json_response['properties']['Due']['date']:
        due_by = api_json_response['properties']['Due']['date']['end']
    else:
        due_by = None

    if not api_json_response['properties']['Task']['title']:
        a = 3

    return Task(
        title=api_json_response['properties']['Task']['title'][0]['text']['content'],
        due_by=due_by,
    )


def as_tasks(api_json_response: dict) -> list[Task]:
    return [as_task(json) for json in api_json_response['results']]
