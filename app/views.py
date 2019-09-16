from django.shortcuts import render
from scrapy import cmdline
from spider.spider.test import urls, X_Path
import threading


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def spiders(request):
    if request.method == 'POST':
        print(request.POST.get('ip'))
        t = threading.Thread(target=Spider)
        t.run()
    return render(request, 'index.html', {})


def Spider():
    urls.URLS.append('https://movie.douban.com/top250')
    X_Path.path = '//*[@id="content"]/div/div/ol/li/div/div/div/a/span[1]' + '/text()'
    cmdline.execute('scrapy crawl myspider'.split())
