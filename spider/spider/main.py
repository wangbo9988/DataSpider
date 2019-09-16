from scrapy import cmdline
from urllib.parse import urlparse
import re

from urllib.parse import urlparse

from spider.spider.test import urls

urls.URLS.append('https://movie.douban.com/top250')

cmdline.execute('scrapy crawl accurateSpider'.split())
