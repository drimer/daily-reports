from datetime import datetime, timedelta

import requests

from src.pokemon.config import PokemonConfig
from src.pokemon.models import PokemonNewsItem


class PokemonNewsApiClient:
    def __init__(self, pokemon_config: PokemonConfig):
        self.api_token = pokemon_config.NEWS_API_TOKEN

    def get_request_headers(self):
        return {
            "Authorization": "Bearer " + self.api_token,
        }

    def get_latest_pokemon_news(self):
        url = 'https://newsapi.org/v2/everything'
        from_param = (datetime.utcnow() - timedelta(days=3)).strftime('%Y-%m-%d')

        params = {
            'q': '+pokemon -TCG -"Pokemon Go" -"Pok%C3%A9mon GO"',
            'from': from_param,
            'sortBy': 'publishedAt',
            'excludeDomains': 'businessinsider.com,sky.com,prtimes.jp,biztoc.com',
            'searchIn': 'title,description',
            'language': 'en',
        }
        res = requests.request("GET", url, headers=self.get_request_headers(), params=params)
        data = res.json()
        return data

    def as_pokemon_news_item(self, api_json_response: dict) -> PokemonNewsItem:
        return PokemonNewsItem(title=api_json_response['title'], url=api_json_response['url'])

    def as_pokemon_news_items(self, api_json_response: dict) -> list[PokemonNewsItem]:
        return [self.as_pokemon_news_item(json) for json in api_json_response['articles']]
