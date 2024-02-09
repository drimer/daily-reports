from src.config import Config


class PokemonConfig(Config):
    NEWS_API_TOKEN: str = None

    def __init__(self) -> None:
        super().__init__()

        self.NEWS_API_TOKEN = self.get_from_env('NEWS_API_TOKEN')
