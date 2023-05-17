from functools import cache
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class Url:

    def __init__(self, url: str):
        self.url = url
        self._parsed_url = urlparse(url)
        self._html = None
        self._soup = None

    def is_valid(self) -> bool:
        return all([self._parsed_url.scheme, self._parsed_url.netloc])

    def is_https(self) -> bool:
        return self._parsed_url.scheme == 'https'

    def is_www(self) -> bool:
        return 'www' in self._parsed_url.netloc

    @cache
    def html(self) -> str:
        return requests.get(self.url).text

    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.html(), 'html.parser')
