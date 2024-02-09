from src.config import Config


class ReportSendersConfig(Config):
    FROM_EMAIL_ADDRESS: str = None
    FROM_EMAIL_PASSWORD: str = None
    RECIPIENT_EMAIL_ADDRESS: str = None

    def __init__(self) -> None:
        super().__init__()

        self.FROM_EMAIL_ADDRESS = self.get_from_env('FROM_EMAIL_ADDRESS')
        self.FROM_EMAIL_PASSWORD = self.get_from_env('FROM_EMAIL_PASSWORD')
        self.RECIPIENT_EMAIL_ADDRESS = self.get_from_env('RECIPIENT_EMAIL_ADDRESS')
