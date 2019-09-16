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
    url = "www.csdn.net"

    def start_requests(self):
        urls = [
            'http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/html/A0101a.htm',
        ]
        for i in urls:
            yield scrapy.Request(url=i, method='POST', callback=self.parse_post)

    # 页面解析
    def parse_post(self, response):
        data_list = response.xpath("//table//tr[contains(@style,'mso-height-source')]").extract()

        for i_item in data_list:
            print(i_item)
