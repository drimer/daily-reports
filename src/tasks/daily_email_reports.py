import abc
from typing import Callable

from dependency_injector.wiring import inject, Provide
from src.core.reports import ReportRunner, ReportSender

from src.di_container import DIContainer
from src.notion.reports import NotionReportRunner


def _task(
        report_runners: list[ReportRunner],
        email_report_sender: ReportSender,
):
    # report_runners: list[ReportRunner] = [notion_report_runner(), pokemon_report_runner()]
    
    try:
        reports = [runner.run() for runner in report_runners]
    except Exception as e:
        print(f'Error trying to run: {report_runners}')
        raise e

    try:
        email_report_sender.send(reports)
    except Exception as e:
        print(f'Error trying to send: {reports}')
        raise e


def task():
    container = DIContainer()
    container.wire(modules=[__name__])
    
    report_runners: list[ReportRunner] = []
    for attribute_name in dir(container):
        try:
            instance = getattr(container, attribute_name)()
            if isinstance(instance, ReportRunner):
                report_runners.append(instance)    
        except Exception:
            continue
    
    _task(report_runners, container.email_report_sender())


if __name__ == '__main__':
    task()
