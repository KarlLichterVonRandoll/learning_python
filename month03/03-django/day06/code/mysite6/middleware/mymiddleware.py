from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, Http404
import re


class VisitLimit(MiddlewareMixin):
    """
        此中间件限制一个IP地址对应的访问 /user/login 的次数不能改过10次,
        超过后禁止使用
    """
    visit_times = {}  # 记录用户访问次数

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']  # 得到IP地址
        if not re.match(r'^/test', request.path_info):
            return
        times = self.visit_times.get(ip_address, 0)
        print("IP:", ip_address, "已经访问了", times, "次", request.path_info)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return

        return HttpResponse('你已经访问了' + str(times) + '次,禁止访问了')
