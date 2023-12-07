from src.config import Config


class ReportSendersConfig(Config):
    FROM_EMAIL_ADDRESS = Config.get_from_env('FROM_EMAIL_ADDRESS')
    FROM_EMAIL_PASSWORD = Config.get_from_env('FROM_EMAIL_PASSWORD')
    RECIPIENT_EMAIL_ADDRESS = Config.get_from_env('RECIPIENT_EMAIL_ADDRESS')


if __name__ == '__main__':
    config = ReportSendersConfig()
