from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404


def index_view(request):
    print("主页被访问")
    return HttpResponse("这是主页")


def page1_view(request):
    # return HttpResponse("这是页面1")
    raise Http404


def xxx_view(request):
    raise Http404
