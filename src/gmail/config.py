from src.config import Config


class GmailConfig(Config):
    EMAIL_ADDRESS: str = None
    PASSWORD: str = None
    OLDER_THAN_DAYS: str = None

    def __init__(self) -> None:
        super().__init__()

        self.EMAIL_ADDRESS = self.get_from_env("GMAIL_EMAIL_ADDRESS")
        self.PASSWORD = self.get_from_env("GMAIL_PASSWORD")
        self.OLDER_THAN_DAYS = self.get_from_env("GMAIL_OLDER_THAN_DAYS")
