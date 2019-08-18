from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app01$', views.app01_view)
]
