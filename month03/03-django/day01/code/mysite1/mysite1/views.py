# file: mysite1/views.py
from django.http import HttpResponse, HttpResponseRedirect


def page1_view(request):
    html = "<h1>这是第一个页面</h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是第二个页面</h1>"
    return HttpResponseRedirect("https://www.baidu.com")


def index_view(request):
    html = "<h1>主页</h1>"
    return HttpResponse(html)


def pagen_view(request, n):
    html = "<h1>这是第%s个页面</h1>" % n
    return HttpResponse(html)


def cal_view(request, x, op, y):
    if op == "add":
        result = eval(x + "+" + y)
    elif op == "sub":
        result = eval(x + "-" + y)
    elif op == "mul":
        result = eval(x + "*" + y)
    else:
        return HttpResponse("<h1>出错了</h1>")
    return HttpResponse("<h1>结果是：" + str(result) + "</h1>")


def person_view(request, **kwargs):
    name = str(kwargs['name'])
    age = str(kwargs['age'])
    result = "<h1>%s:%s</h1>" % (name, age)

    return HttpResponse(result)


def birthday_view(request, **kwargs):
    print(request.method)
    result = "<h1>%s年%s月%s日</h1>" % (kwargs['y'], kwargs['m'], kwargs['d'])

    return HttpResponse(result)


def mypage_view(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    result = "<h1>a=%s,b=%s</h1>" % (a, b)
    return HttpResponse(result)


def sum_view(request):
    if request.method == "GET":
        start = int(request.GET.get('start', 2))
        step = int(request.GET['step'])
        stop = int(request.GET['stop'])
        sum = 0
        for i in range(start, stop, step):
            sum += i
        result = "<h1>%d</h1>" % sum
        return HttpResponse(result)
    else:
        return HttpResponse("当前不是 get 请求")


def birthday_view2(request):
    if request.method == "GET":
        y = request.GET['y']
        m = request.GET['m']
        d = request.GET['d']
        result = "<h1>%s年%s月%s日</h1>" % (y, m, d)
        return HttpResponse(result)
    else:
        return HttpResponse("error")
