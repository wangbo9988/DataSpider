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


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.csdn.net/nav/java']

    url = "www.csdn.net"

    data = {}

    # 页面解析
    def parse(self, response):

        movie_list = response.xpath('/html').extract()

        for temp in movie_list:
            soup = BeautifulSoup(temp, 'html5lib')
            # print(soup.title)
            # print(soup.title.name)
            # print(soup.title.string)
            # print(soup.title.parent.name)
            # print(soup.p)
            # print(soup.p['class'])
            # print(soup.p.string)
            # print(soup.a)
            # links = soup.find_all('a')
            # for i in links:
            #     print(i.get('href'))
            # #     从文档中获取所有文字内容:
            # print(soup.get_text())

            # 提取网址
            urls = []
            for link in soup.find_all('a'):
                urls.append(link.get('href'))

            # 提取table内容
            tables = []
            table_node = soup.find_all('td')
            for table in table_node:
                tables.append(table.get_text())

            # 提取ul内容
            datas = {}
            doc = py(temp)
            item = doc('div ul li')
            for li in item.items():
                datas['img'] = li.find('img')
                datas['url'] = li.find('a')
                datas['content'] = li.text()
