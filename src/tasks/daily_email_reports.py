import src.notion.reports
import src.pokemon.reports
from src.report_senders import email_reporter


def task():
    notion_daily_report = src.notion.reports.build_daily_report()
    pokemon_news_report = src.pokemon.reports.build_daily_report()
    reports = [notion_daily_report, pokemon_news_report]

    email_reporter.send(reports)


if __name__ == '__main__':
    task()
