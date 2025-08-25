from typing import Callable

from dependency_injector.wiring import Provide, inject

from src.di_container import DIContainer


@inject
def _task(
    gmail_delete_old_emails: Callable = Provide[
        DIContainer.gmail_delete_old_emails.provider
    ],
):
    print("Cleaning up old emails...")
    gmail_delete_old_emails()


def task():
    container = DIContainer()
    container.wire(modules=[__name__])
    _task()


if __name__ == "__main__":
    task()
