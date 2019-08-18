from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_cookie', views.get_cookie),
]
