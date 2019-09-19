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
    start_urls = [
        'https://cn.bing.com/search?q=BeautifulSoup&qs=n&form=QBRE&sp=-1&pq=beautifulsoup&sc=8-13&sk=&cvid=0CA66B777B904FCD9C5DA73671C8F45F']

    url = "www.bing.com"

    data = {}

    # 页面解析
    def parse(self, response):

        movie_list = response.xpath('/html').extract()

        for temp in movie_list:
            soup = BeautifulSoup(temp, 'html5lib')

            # 提取网址
            urls = []
            for link in soup.find_all('a'):
                urls.append(link.get('href'))

            # 提取ul内容
            datas1 = {}
            doc = py(temp)
            item = doc('ul li')
            for li in item:
                datas1['img'] = li.find('img')
                datas1['url'] = li.find('a').attr('href')
                datas1['content'] = li.text()

            # 提取ol内容
            datas2 = {}
            doc = py(temp)
            item = doc('div ol li')
            for li in item.items():
                datas2['img'] = li.find('img')
                datas2['url'] = li.find('a').attr('href')
                datas2['content'] = li.text()

            # 提取自定义列表内容
            datas3 = {}
            doc = py(temp)
            item = doc('dl')
            for t in item.items():
                datas3['dt'] = t.find('dt').text()
                dd = []
                for tt in t.find('dd').items():
                    dd.append(tt.text())
                datas3['dd'] = dd

            # 提取table内容
            tables = []
            table_node = soup.find_all('td')
            for table in table_node:
                tables.append(table.get_text())
