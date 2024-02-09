from src.core.reports import Report, ReportRunner
from src.pokemon.models import PokemonNewsReport
from src.pokemon.news_api_client import PokemonNewsApiClient


class PokemonNewsReportRunner(ReportRunner):
    def __init__(self, api_client: PokemonNewsApiClient) -> None:
        self.api_client = api_client

    def run(self) -> Report:
        articles_response = self.api_client.get_latest_pokemon_news()
        news_items = self.api_client.as_pokemon_news_items(articles_response)
        return PokemonNewsReport(news_items=news_items)
