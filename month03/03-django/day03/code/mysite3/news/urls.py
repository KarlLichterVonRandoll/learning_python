"""
    此模块实现 news 应用中的子路由配置
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index_view),
]