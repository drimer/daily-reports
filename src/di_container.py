from dependency_injector import containers, providers

import src.notion.reports
import src.pokemon.reports
from src.report_senders.email_reporter import send


class DIContainer(containers.DeclarativeContainer):
    notion_report_builder = providers.Callable(
        src.notion.reports.build_daily_report
    )
    pokemon_report_builder = providers.Callable(
        src.pokemon.reports.build_daily_report
    )

    email_report_sender = providers.Callable(send)
