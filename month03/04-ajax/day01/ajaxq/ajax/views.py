from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def load_test(request):
    return render(request, 'load_test.html')


def load_test_server(request):
    return render(request, 'load_test_server.html')


def jquery_get(request):
    return render(request, 'jquery_get.html')


def jquery_get_server(request):
    uname = request.GET.get('uname', 'null')
    age = request.GET.get('age', 'null')

    d = {'uname': uname, 'age': age}

    # 指定HttpResponse响应头
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_post(request):
    return render(request, 'jquery_post.html')


def jquery_post_server(request):
    d = {'msg': 'post is ok', 'code': 200}

    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax(request):
    return render(request, 'jquery_ajax.html')


def jquery_ajax_server(request):
    import time
    time.sleep(3)
    d = {'name': 'guo', 'age': 18}

    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_data(request):
    return render(request, 'jquery_data.html')


def jquery_data_server(request):
    data = [
        {'name': 'guo', 'age': 18},
        {'name': 'wei', 'age': 20},
    ]
    return HttpResponse(json.dumps(data), content_type='application/json')


def cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')

    return HttpResponse(func + "('wo lai le')")
