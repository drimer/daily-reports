from src.pokemon.models import PokemonNewsReport
from src.pokemon.news_api_client import get_latest_pokemon_news, as_pokemon_news_items


def build_daily_report():
    articles_response = get_latest_pokemon_news()
    news_items = as_pokemon_news_items(articles_response)
    return PokemonNewsReport(news_items=news_items)


if __name__ == '__main__':
    build_daily_report()
