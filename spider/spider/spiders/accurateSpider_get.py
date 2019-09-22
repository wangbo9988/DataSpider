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
from spider.spider.spiders import configs

import os
import re


class MyspiderSpider(scrapy.Spider):
    name = 'accurateSpider_get'
    start_urls = configs.URLS

    url = configs.DOMAIN_NAME

    data = {}

    # 页面解析
    def parse(self, response):
        movie_list = response.xpath('//*[@id="tabcont"]/table').extract()
        print(movie_list)
        # for temp in movie_list:
        #     tt = temp.xpath('.//td').extract()
        #     for i in tt:
        #         print(py(i).text())
        #     print('——' * 80)
