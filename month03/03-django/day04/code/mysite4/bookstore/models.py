from django.db import models


# Create your models here.
# class Author(models.Model):
#     ...

class Book(models.Model):
    title = models.CharField(max_length=30,
                             null=False,
                             unique=True,
                             verbose_name='书名')  # varchar(30)
    pub = models.CharField(max_length=50,
                           verbose_name='出版社',
                           null=True
                           )
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                default=88888,
                                verbose_name='定价')  # Decimal(7, 2)
    market_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='零售价',
        default='99999'
    )

    def __str__(self):
        return "书名：%s 出版社：%s 定价：%s 零售价：%s" % (self.title, self.pub, self.price, self.market_price)

    class Meta:
        db_table = 'mybook'


class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=30)
    age = models.IntegerField(verbose_name='年龄', default=1)
    email = models.EmailField(verbose_name='邮箱', default="XX@yy.cn")

    # 1. name - CharField 姓名,非空
    # 2. age - IntegerField, 年龄,非空，缺省值为1
    # 3. email - EmailField, 邮箱,允许为空

    def __str__(self):
        return "姓名：%s  年龄：%s  邮箱：%s" % (self.name, self.age, self.email)

    class Meta:
        db_table = 'myauthor'


class Wife(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    author = models.OneToOneField(Author)  # 增加一对一属性


# class Publisher(models.Model):
#     '''出版社'''
#     name = models.

