# mysite2/views.py

from django.http import HttpResponse
from django.shortcuts import render

login_form_html = """
    <form method="post" action="/login">
        姓名:<input type="text" name="username">
        <input type="submit" value="提交">
    </form>

"""

login_form_html2 = """
    <form action="/login" method="POST">
        <input name="title" type="text" value="请输入">
        <select name="gender">
            <option value=1>男</option>
            <option value=0>女</option>
        </select>
        <textarea name="comment" rows="5" cols="10">附言...</textarea>
        <input type="submit" value="提交">
    </form>
"""


def sum_view(request):
    if request.method == "GET":
        start = int(request.GET.get('start', '0'))
        step = int(request.GET.get('step', '1'))
        stop = int(request.GET['stop'])
        sum = 0
        for i in range(start, stop, step):
            sum += i
        result = "<h1>%d</h1>" % sum
        return HttpResponse(result)
    else:
        return HttpResponse("当前不是 get 请求")


def login_view(request):
    if request.method == "GET":
        return HttpResponse(login_form_html2)
    elif request.method == "POST":
        name = request.POST.get('username', '属性错误')
        return HttpResponse(str(dict((request.POST))))


def login2_view(request):
    if request.method == "GET":
        # 返回模板生成的html给浏览器
        # 方法1：
        # 1.先加载模板
        # from django.template import loader
        # t = loader.get_template("mylogin.html")
        # # 2.用模板生成html
        # html = t.render({"name": 'tarena'})
        # # 3.将html返回给浏览器
        # return HttpResponse(html)

        # 方法2：
        # 使用 render() 直接加载并响应模板
        return render(request, 'mylogin.html', {"name": "tarena"})


def mytemp_view(request):
    # dict = {
    #     "x": 0,
    # }
    x = -5
    return render(request, 'mytemp.html', locals())


def mycal_view(request):
    if request.method == "GET":
        return render(request, "mycal.html")
    elif request.method == "POST":
        btn = request.POST['btn']
        if btn == "重置":
            return render(request, "mycal.html")
        x = request.POST.get('x', '0')
        opp = request.POST['opp']
        y = request.POST.get('y', '0')
        if opp == "/" and y == "0":
            return render(request, "mycal.html", {"result": "ZeroDivisionError"})
        result = eval(x + opp + y)
        return render(request, 'mycal.html', locals())


def for_view(request):
    lst = ['北京', '上海', '杭州']
    s = "<b>Hello World</b>"
    ss = "helloworld"
    n = 100
    print(locals())
    return render(request, "for.html", locals())


def index_view(request):
    return render(request, "base.html")


def sport_view(request):
    return render(request, "sport.html")


def news_view(request):
    return render(request, "news.html")


def pagen_view(request, n):
    return HttpResponse("第" + n + "页")
