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
        if not self.tasks:
            message = '<div>You\'re all done for today. Congratulations!</div>'
        else:
            message = '<ul>{}</ul>'.format(
                ''.join(
                    ('<li>"{}" due by {}</li>'.format(task.title, task.due_by) for task in self.tasks)
                )
            )

        return '''
        <p><b>Tasks in Notion</b><p>
        {}
        '''.format(message)
