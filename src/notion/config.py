from src.config import Config


class NotionConfig(Config):
    NOTION_API_TOKEN: str = None
    NOTION_TASKS_DB_ID: str = None

    def __init__(self) -> None:
        super().__init__()

        self.NOTION_API_TOKEN = self.get_from_env('NOTION_API_TOKEN')
        self.NOTION_TASKS_DB_ID = self.get_from_env('NOTION_TASKS_DB_ID')
