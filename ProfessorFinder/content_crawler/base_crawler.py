import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    def __init__(self, url, test=False):
        self._url = url
        self._internal_link_parse()     # parse link
        if not test:
            self._page = self._get_page()
            if self._page is None:
                print('error')
            self.bs = BeautifulSoup(self._page.text, 'lxml')

    def handler(self):
        """
        needs to be overwritten,
        return school, department, name, email, bio of teacher.
        :return:
        """
        pass

    def run(self):
        return self.handler()

    def _internal_link_convert(self, raw_link: str):
        if raw_link.startswith('/'):
            return self._scheme + '://' + self._netloc + raw_link
        elif re.match('^http(s)?://.+', raw_link):
            return raw_link
        else:
            return self._scheme + '://' + raw_link

    def _internal_link_parse(self):
        o = urlparse(self._url)
        self._scheme = o.scheme
        self._netloc = o.netloc

    def _get_page(self):
        try:
            response = requests.get(self._url)
        except requests.exceptions.HTTPError:
            response = None
        return response
