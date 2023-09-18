import datetime
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Task:
    title: str
    due_by: datetime.datetime = None


@dataclass
class EmailReport:
    tasks: Iterable[Task]

    def __str__(self):
        return '''
        <p><b>Tasks in Notion</b><p>
        <ul>{}</ul>
        '''.format(
            ''.join(
                ('<li>"{}" due by {}</li>'.format(task.title, task.due_by) for task in self.tasks)
            )
        )
