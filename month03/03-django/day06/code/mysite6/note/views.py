from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.

# file: note/views.py

from user.models import User
from . import models
from django.core.paginator import Paginator


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):  # 没有登陆
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:  # 没有登陆
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)

    return wrap


def list_view(request):
    if not hasattr(request, 'session'):  # 没有登陆
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:  # 没有登陆
        return HttpResponseRedirect('/user/login')
    # 此时一定已登陆
    user_id = request.session['user']['id']
    # 根据已登陆的用户id 找到当前登陆的用户
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    return render(request, 'note/showall.html', locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        # 得到当前用户的信息
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = models.Note(user=auser)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')


@check_login
def mod_view(request, id):
    # 得到当前登陆的用户的模型对象
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    if request.method == 'GET':
        return render(request, 'note/mod_note.html',
                      locals())
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note')


def del_view(request, id):
    # 得到当前登陆的用户的模型对象
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    anote.delete()
    return HttpResponseRedirect('/note')


def list2_view(request):
    if not hasattr(request, 'session'):  # 没有登陆
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:  # 没有登陆
        return HttpResponseRedirect('/user/login')
    # 此时一定已登陆
    user_id = request.session['user']['id']
    # 根据已登陆的用户id 找到当前登陆的用户
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    # 在此处添加分页功能
    paginator = Paginator(notes, 5)
    # print('当前对象的总个数是:', paginator.count)
    # print('当前对象的面码范围是:', paginator.page_range)
    # print('总页数是：', paginator.num_pages)
    # print('每页最大个数:', paginator.per_page)
    cur_page = int(request.GET.get('page', 1))  # 得到默认的当前页
    page = paginator.page(cur_page)
    return render(request, 'note/listpage.html', locals())



