from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(verbose_name='出版社', max_length=30)

    def __str__(self):
        return "出版社：%s"%self.name

    class Meta:
        db_table = 'mypub'


class Book2(models.Model):
    title = models.CharField(max_length=30, verbose_name="书名")

    publisher = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return "书名2：%s"%self.title

    class Meta:
        db_table = 'mybook2'

