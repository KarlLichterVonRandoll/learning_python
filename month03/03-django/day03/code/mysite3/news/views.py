from django.shortcuts import render

# Create your views here.

# news/views.py
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("新闻主页")

