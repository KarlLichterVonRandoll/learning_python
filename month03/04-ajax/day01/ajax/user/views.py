from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import User


def xhr(request):
    return render(request, 'xhr.html')


def get_xhr(request):
    return render(request, 'get-xhr.html')


def get_xhr_server(request):
    if request.GET.get('uname'):
        uname = request.GET['uname']
        return HttpResponse('welcome  %s' % (uname))
    return HttpResponse('This is ajax request !')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        uname = request.POST.get('uname')
        if not uname:
            return HttpResponse("请输入用户名")
        pwd = request.POST.get('pwd')
        if not pwd:
            return HttpResponse("请输入密码")
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse("请输入昵称")
        User.objects.create(uname=uname, pwd=pwd, nickname=nickname)
        return HttpResponse("注册成功")
    else:
        raise Http404


def checkuname(request):
    # 1　获取ajax传过来的用户名
    uname = request.GET.get('uname')
    # 2 校验用户名是否存在
    users = User.objects.filter(uname=uname)
    if users:
        return HttpResponse('1')
    return HttpResponse('0')


def makepost(request):
    if request.method == "GET":
        return render(request, 'makepost.html')
    elif request.method == "POST":
        # 获取表单数据
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        print(uname, "=========")
        return HttpResponse("uname %s, pwd %s" % (uname, pwd))
    else:
        raise Http404


def get_user(request):
    return render(request, 'getuser.html')


def get_user_server(request):
    users = User.objects.all()
    char = ""
    for u in users:
        char += "%s_%s_%s|" % (u.uname, u.pwd, u.nickname)
    msg = char[:-1]

    return HttpResponse(msg)


def json_obj(request):
    return render(request, 'json_obj.html')


def json_dumps(request):
    # 1.生成单个对象的json字符串/ 序列化 -> obj - str
    # 反序列化 -> str -> obj
    dic = {
        'uname': 'Lili',
        'uage': '30'
    }
    import json

    # sort_keys=True 使输出有序
    # separators:参数("xx","xx"),第一个参数指的是每一个键值对之间用当前参数分割；第二个参数指的是每一个
    # 键值对中的建与值之间用当前参数分隔。
    json_str = json.dumps(dic, sort_keys=True, separators=(',', ":"))

    # 2.生成多个对象的json字符串
    s = [
        {
            'uname': 'lucy',
            'age': 18
        },
        {
            'uname': '胖虎',
            'age': 20
        }
    ]
    json_str_arr = json.dumps(s, sort_keys=True, separators=(',', ":"))

    from django.core import serializers
    users = User.objects.all()
    json_str_all = serializers.serialize('json', users)

    return JsonResponse(dic)
    # return HttpResponse(json_str_all, content_type='application/json')
