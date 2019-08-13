# mysite2/views.py

from django.http import HttpResponse

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