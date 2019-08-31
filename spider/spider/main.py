from scrapy import cmdline
from spider.test import urls, X_Path

urls.URLS.append('https://movie.douban.com/top250')
X_Path.path = '//*[@id="content"]/div/div/ol/li/div/div/div/a/span[1]' + '/text()'

cmdline.execute('scrapy crawl myspider'.split())
