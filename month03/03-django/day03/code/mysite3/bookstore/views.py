from django.shortcuts import render

# Create your views here.

# file bookstore/views.py
from django.http import HttpResponse
from . import models


def add_view(request):
    try:
        # 方法一
        # abook = models.Book.objects.create(
        #     title="python", price=50
        # )

        # 方法二
        abook = models.Book()
        abook.title = "Java"
        abook.save()  # 真正执行sql语句
        return HttpResponse("<h1>添加图书成功!</h1>")
    except:
        return HttpResponse("<h1>添加图书失败!</h1>")


def aut_view(request):
    pass
