from django.db import models


# Create your models here.

# 创建类对应数据库的表
class Book(models.Model):
    # 创建类属性对应字段
    title = models.CharField(verbose_name="书名",
                             max_length=30,
                             null=False)  # varchar(30)
    pub = models.CharField(verbose_name="出版社",
                           max_length=30,
                           null=False,
                           default="XXX出版社")
    price = models.DecimalField(verbose_name="价格",
                                max_digits=7,
                                decimal_places=2,
                                default=0.0)  # deciaml(7,2)
    market_price = models.DecimalField(verbose_name="零售价",
                                       max_digits=7,
                                       decimal_places=2,
                                       default=0.0)


class Author(models.Model):
    name = models.CharField(verbose_name="姓名",
                            max_length=20,
                            null=False)
    age = models.IntegerField(verbose_name="年龄",
                              null=False)
    email = models.EmailField(verbose_name="邮箱",
                              max_length=30,
                              null=True)
