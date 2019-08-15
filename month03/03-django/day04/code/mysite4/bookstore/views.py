from django.shortcuts import render

# Create your views here.

# file bookstore/views.py
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


def add_view(request):
    if request.method == "GET":
        return render(request, 'bookstore/add_book.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price'))
        market_price = request.POST.get('market_price')
        try:
            models.Book.objects.create(title=title,
                                       pub=pub,
                                       price=price,
                                       market_price=market_price)
            return HttpResponseRedirect("/bookstore/all")
        except:
            return HttpResponse('<h1>添加失败</h1>')


def show_all(request):
    books = models.Book.objects.all()

    return render(request, 'bookstore/list.html', locals())


def mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse("没有id为%s的数据记录" % id)

    if request.method == "GET":
        return render(request, "bookstore/mod.html", locals())
    elif request.method == "POST":
        m_price = request.POST.get("market_price", '0')
        abook.market_price = m_price
        abook.save()
        return HttpResponseRedirect("/bookstore/all")


def del_view(request, id):
    book = models.Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('/bookstore/all')
