from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

# file : bookstore/views.py

from . import models


def add_view(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price', '0'))
        m_price = float(request.POST.get('m_price', '0'))
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=m_price
            )
            # return HttpResponse("添加成功！")
            return HttpResponseRedirect('/bookstore/all')
        except:
            return HttpResponse('添加失败！')


def show_all(request):
    books = models.Book.objects.all()
    # books = models.Book.objects.filter(price__gt=50)  # __gt
    # books = models.Book.objects.filter(price__range=(50, 80))
    # books = models.Book.objects.exclude(pub__contains='清华大学')
    # books = models.Book.objects.exclude(
    #     pub__contains='清华大学', market_price__lt=40)
    # for abook in books:0
    #     print("书名：" + abook.title)
    # return HttpResponse("查询成功")
    return render(request, 'bookstore/list.html', locals())


def mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有id为" + id + "的数据记录")

    if request.method == 'GET':
        return render(request, 'bookstore/mod.html',
                      locals())
    elif request.method == 'POST':
        m_price = float(request.POST.get('m_price', '0'))
        abook.market_price = m_price  # 修改字段的值
        abook.save()
        return HttpResponseRedirect('/bookstore/all')
        # return HttpResponseRedirect('../all')


def del_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse('删除失败！')
    abook.delete()
    return HttpResponseRedirect('/bookstore/all')


def set_cookie(request):
    resp = HttpResponse("ok")
    resp.set_cookie('mycookie', 'aaaaa', 10000)

    return resp


def get_cookie(request):
    value = request.COOKIES.get("mycookie")

    return HttpResponse(value)
