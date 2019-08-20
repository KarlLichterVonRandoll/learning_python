from django.shortcuts import render
from django.conf import settings
import os


# Create your views here.
# file: index/views.py

def index_view(request):
    return render(request, 'index/index.html', locals())


from django.http import HttpResponse


def test_view(request):
    return HttpResponse("转到test")


def upload_view(request):
    if request.method == "GET":
        return render(request, 'index/upload.html', locals())
    elif request.method == "POST":
        a_file = request.FILES['myfile']
        print("上传文件名称：", a_file.name)

        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as f:
            data = a_file.file.read()
            f.write(data)
            return HttpResponse("接收文件:" + a_file.name + "成功")
    raise HttpResponse("文件上传失败！")


