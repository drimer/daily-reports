import abc
from typing import Callable

from dependency_injector.wiring import inject, Provide
from src.core.reports import ReportRunner

from src.di_container import DIContainer
from src.notion.reports import NotionReportRunner


@inject
def _task(
        notion_report_runner: NotionReportRunner = Provide[DIContainer.notion_report_runner.provider],
        pokemon_report_runner: Callable = Provide[DIContainer.pokemon_report_runner.provider],
        email_report_sender: Callable = Provide[DIContainer.email_report_sender.provider],
):
    report_runners: list[ReportRunner] = [notion_report_runner(), pokemon_report_runner()]
    
    try:
        reports = [runner.run() for runner in report_runners]
    except Exception as e:
        print(f'Error trying to run: {report_runners}')
        raise e

    try:
        email_report_sender(reports)
    except Exception as e:
        print(f'Error trying to send: {reports}')
        raise e


def task():
    container = DIContainer()
    container.wire(modules=[__name__])
    _task()


if __name__ == '__main__':
    task()
