from typing import Callable

from dependency_injector.wiring import inject, Provide

from src.di_container import DIContainer


@inject
def _task(
        notion_report_builder: Callable = Provide[DIContainer.notion_report_builder.provider],
        pokemon_report_builder: Callable = Provide[DIContainer.pokemon_report_builder.provider],
        email_report_sender: Callable = Provide[DIContainer.email_report_sender.provider],
):
    reports = [notion_report_builder(), pokemon_report_builder()]

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
