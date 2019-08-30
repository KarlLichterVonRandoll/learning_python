from django.db import models


# Create your models here.

class Author3(models.Model):
    '''作家模型类'''
    name = models.CharField('作家', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'myauthor3'


class Book3(models.Model):
    title = models.CharField('书名', max_length=50)
    author = models.ManyToManyField(Author3)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'mybook3'
