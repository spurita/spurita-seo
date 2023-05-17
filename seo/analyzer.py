from functools import cache

import requests

from seo.url import Url


class AnalyzerConfiguration:

    def __init__(self, title: bool = True, description: bool = True, h: bool = True,
                 broken_links: bool = False):
        self.title = title
        self.description = description
        self.h = h
        self.broken_links = broken_links


class Analyzer:

    def __init__(self, url: str, configuration: AnalyzerConfiguration):
        self._url = Url(url)
        self._config = configuration

    @cache
    def _soup(self):
        return self._url.soup()

    def _title(self):
        if self._config.title:
            s = self._soup()
            title_tag = s.title
            if title_tag:
                return title_tag.text

    def _description(self):
        if self._config.description:
            s = self._soup()
            description_tag = s.find('meta', attrs={'name': 'description'})
            if description_tag:
                return description_tag["content"]

    def _h(self):
        if self._config.h:
            s = self._soup()
            return {
                "h1": len(s.find_all('h1')),
                "h2": len(s.find_all('h2')),
                "h3": len(s.find_all('h3')),
                "h4": len(s.find_all('h4')),
                "h5": len(s.find_all('h5')),
                "h6": len(s.find_all('h6'))
            }

    def _broken_links(self):
        if self._config.broken_links:
            s = self._soup()
            broken_links = 0
            for link in s.find_all('a'):
                if link.get('href'):
                    try:
                        link = link.get('href')
                        link_req = requests.head(link, allow_redirects=True)
                        if link_req.status_code >= 400:
                            broken_links += 1
                    except requests.exceptions.RequestException as e:
                        broken_links += 1
            return broken_links

    def report(self):
        report = {
            "title": self._title(),
            "description": self._description(),
            "h": self._h(),
            "broken_links": self._broken_links()
        }
        return report
