# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from scrapy.selector import Selector
from spider.spider.test import X_Path
from urllib.parse import urlparse
from spider.spider.test import urls
from spider.spider.items import SpiderItem
from bs4 import BeautifulSoup
from pyquery import PyQuery as py

import os
import re


class AccurateSpider(scrapy.Spider):
    name = 'accurateSpider'
    url = "www.github.com"

    def start_requests(self):
        urls = [
            'https://github.com/search?p=2&q=universal+crawler&type=Repositories',
        ]
        for i in urls:
            yield scrapy.Request(url=i, method='POST', callback=self.parse_post)

    # 页面解析
    def parse_post(self, response):
        data_list = response.xpath("//table//tr[contains(@style,'mso-height-source')]").extract()

        for i_item in data_list:
            soup = BeautifulSoup(i_item, 'html5lib')
            print(soup.text)

