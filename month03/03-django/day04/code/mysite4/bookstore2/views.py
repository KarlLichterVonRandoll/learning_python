from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_cookie(request):
    value = request.COOKIES.get("mycookie")

    return HttpResponse(value)
