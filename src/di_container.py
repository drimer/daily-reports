from dependency_injector import containers, providers
from src.notion.reports import NotionReportRunner

from src.pokemon.config import PokemonConfig
from src.pokemon.news_api_client import PokemonNewsApiClient
from src.notion.api_client import NotionApiClient
from src.notion.config import NotionConfig
from src.pokemon.reports import PokemonNewsReportRunner
from src.report_senders.config import ReportSendersConfig
from src.report_senders.email_reporter import EmailReportSender


class DIContainer(containers.DeclarativeContainer):
    # Notion
    notion_config = providers.Factory(NotionConfig)
    notion_api_client = providers.Singleton(NotionApiClient, notion_config)
    notion_report_runner = providers.Factory(
        NotionReportRunner, notion_api_client
    )

    # Report builders
    pokemon_config = providers.Factory(PokemonConfig)
    pokemon_news_api_client = providers.Factory(
        PokemonNewsApiClient, pokemon_config
    )
    pokemon_report_runner = providers.Factory(
        PokemonNewsReportRunner, pokemon_news_api_client
    )

    # Report senders
    report_senders_config = providers.Factory(ReportSendersConfig)
    email_report_sender = providers.Factory(EmailReportSender, report_senders_config)
