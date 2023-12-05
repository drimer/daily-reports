from dependency_injector import containers, providers

import src.notion.reports
import src.pokemon.reports
from src.notion.api_client import NotionApiClient
from src.notion.config import NotionConfig
from src.report_senders.email_reporter import send


class DIContainer(containers.DeclarativeContainer):
    # Notion
    notion_config = providers.Factory(NotionConfig)
    notion_report_builder = providers.Callable(
        src.notion.reports.build_daily_report
    )
    notion_api_client = providers.Singleton(NotionApiClient, api_client=notion_config)

    # Report builders
    pokemon_report_builder = providers.Callable(
        src.pokemon.reports.build_daily_report
    )

    # Report senders
    email_report_sender = providers.Callable(send)
