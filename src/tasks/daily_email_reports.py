from dependency_injector import providers

from src.core.reports import ReportRunner, ReportSender
from src.di_container import DIContainer


def _task(
    report_runners: list[ReportRunner],
    email_report_sender: ReportSender,
):
    try:
        reports = [runner.run() for runner in report_runners]
    except Exception as e:
        print(f"Error trying to run: {report_runners}")
        raise e

    try:
        email_report_sender.send(reports)
    except Exception as e:
        print(f"Error trying to send: {reports}")
        raise e


def task():
    container = DIContainer()
    container.wire(modules=[__name__])

    report_runners: list[ReportRunner] = []
    for attribute_name in dir(container):
        try:
            attribute_value = getattr(container, attribute_name)
            if issubclass(type(attribute_value), providers.Provider) and issubclass(
                attribute_value.cls, ReportRunner
            ):
                report_runners.append(attribute_value())
        except Exception:
            continue

    _task(report_runners, container.email_report_sender())


if __name__ == "__main__":
    task()
