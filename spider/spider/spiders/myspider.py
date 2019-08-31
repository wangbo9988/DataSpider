# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from spider.test import X_Path
from spider.test import urls
from spider.items import SpiderItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = urls.URLS

    url = "movie.douban.com"

    # 页面解析
    def parse(self, response):
        movie_list = response.xpath(X_Path.path).extract()
        print(movie_list)
        print('结果========================')
        for i in movie_list:
            demo_item = SpiderItem()
            demo_item['movie_name'] = i
            print(demo_item)
