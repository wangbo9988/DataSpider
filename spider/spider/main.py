from scrapy import cmdline
from urllib.parse import urlparse
import re

from urllib.parse import urlparse

from spider.spider.test import urls

urls.URLS.append('')

cmdline.execute('scrapy crawl myspider'.split())
# cmdline.execute('scrapy crawl accurateSpider'.split())
