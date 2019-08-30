from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def app01_view(request):
    return HttpResponse("app01")
