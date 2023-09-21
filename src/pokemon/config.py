from src.config import Config


class PokemonConfig(Config):
    NEWS_API_TOKEN = Config.get_from_env('NEWS_API_TOKEN')


if __name__ == '__main__':
    config = PokemonConfig()
