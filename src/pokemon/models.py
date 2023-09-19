from dataclasses import dataclass
from typing import Iterable


@dataclass
class PokemonNewsItem:
    title: str
    url: str


@dataclass
class PokemonNewsReport:
    news_items: Iterable[PokemonNewsItem]

    def __str__(self):
        if not self.news_items:
            message = '<div>No news about Pokemon today :(</div>'
        else:
            message = '<ul>{}</ul>'.format(
                ''.join(
                    ('<li><a href="{}">{}</a></li>'.format(item.url, item.title) for item in self.news_items)
                )
            )

        return '''
        <p><b>Pokemon news</b><p>
        {}
        '''.format(message)
