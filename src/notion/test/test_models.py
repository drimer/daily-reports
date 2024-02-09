from datetime import datetime, timedelta

import htmlmin
import pytest

from src.notion.models import Task, EmailReport


@pytest.fixture
def task_in_future():
    return Task(title='Test Task', due_by=datetime.now() + timedelta(days=1))


def test_email_report_returns_nice_message_when_no_tasks():
    expected = '''
    <p><b>Tasks in Notion</b><p>
    <div>You're all done for today. Congratulations!</div>
    '''

    report = EmailReport(tasks=[])

    assert htmlmin.minify(expected) == htmlmin.minify(str(report))


def test_email_report_when_one_task_in_future(task_in_future):
    expected = '''
    <p><b>Tasks in Notion</b><p>
    <ul><li>"{}" due by {}</li></ul>
    '''.format(task_in_future.title, task_in_future.due_by)

    report = EmailReport(tasks=[task_in_future])

    assert htmlmin.minify(expected) == htmlmin.minify(str(report))
