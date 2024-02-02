from dependency_injector import containers, providers

import src.notion.reports
import src.pokemon.reports
from src.notion.api_client import NotionApiClient
from src.notion.config import NotionConfig
from src.report_senders.email_reporter import send


class DIContainer(containers.DeclarativeContainer):
    # Notion
    notion_config = providers.Factory(NotionConfig)
    notion_api_client = providers.Singleton(NotionApiClient, notion_config)
    notion_report_runner = providers.Factory(
        src.notion.reports.NotionReportRunner, notion_api_client
    )

    # Report builders
    pokemon_config = providers.Factory(src.pokemon.config.PokemonConfig)
    pokemon_news_api_client = providers.Factory(
        src.pokemon.news_api_client.PokemonNewsApiClient, pokemon_config
    )
    pokemon_report_runner = providers.Factory(
        src.pokemon.reports.PokemonNewsReportRunner, pokemon_news_api_client
    )

    # Report senders
    email_report_sender = providers.Callable(send)
