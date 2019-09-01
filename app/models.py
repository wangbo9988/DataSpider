from django.db import models


# Create your models here.

class data_spider(models.Model):
    name = models.CharField(max_length=255, verbose_name='名称')
    address = models.CharField(max_length=255, verbose_name='网址')
    content = models.TextField(verbose_name='内容')

    # 该字段的别名
    class Meta():
        verbose_name_plural = '爬虫'

    def __str__(self):
        return self.title
