from src.config import Config


class NotionConfig(Config):
    NOTION_API_TOKEN = Config.get_from_env('NOTION_API_TOKEN')
