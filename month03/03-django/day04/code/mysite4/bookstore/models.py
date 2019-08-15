from django.db import models


# Create your models here.

# 创建类对应数据库的表
class Book(models.Model):
    # 创建类属性对应字段
    title = models.CharField(verbose_name="书名",
                             max_length=30,
                             unique=True,
                             null=False)
    pub = models.CharField(verbose_name="出版社",
                           max_length=50,
                           null=False)
    price = models.DecimalField(verbose_name="定价",
                                max_digits=7,
                                decimal_places=2,
                                null=False)
    market_price = models.DecimalField(verbose_name="零售价",
                                       max_digits=7,
                                       decimal_places=2)

    def __str__(self):
        return "书名: %s, 出版社: %s, 定价: %s" % (self.title, self.pub, self.price)


class Author(models.Model):
    name = models.CharField(verbose_name="姓名",
                            max_length=30)
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱",
                              null=True)
