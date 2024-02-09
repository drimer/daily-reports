from unittest import mock
import pytest
from src.notion.models import Task

from src.notion.reports import NotionReportRunner


@pytest.fixture
def notion_api_client():
    return mock.Mock()


@pytest.fixture
def notion_report_runner(notion_api_client):
    return NotionReportRunner(notion_api_client)


def test_that_notion_report_runner_calls_notion_api_client_with_tasks(
            notion_report_runner, notion_api_client
        ):
    notion_api_client.get_todays_tasks = mock.Mock(return_value={
        'results': [{
            'properties': {
                'Due': {
                    'date': {
                        'start': '2021-08-30',
                        'end': None
                    }
                },
                'Task': {
                    'title': [
                        {'text': {'content': 'Test Task'}}
                    ]
                }
            }
        }]
    })

    report = notion_report_runner.run()

    notion_api_client.get_todays_tasks.assert_called_once()
    assert report.tasks == [
        Task(
            title='Test Task',
            due_by='2021-08-30'
        )
    ]
