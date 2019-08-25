from django.conf.urls import url
from . import views

urlpatterns = [
    # user/xhr/
    url(r'^xhr/$', views.xhr, name='xhr'),
    # user/get-xhr/
    url(r'^get-xhr/$', views.get_xhr, name='get_xhr'),
    # user/get-xhr-server/
    url(r'^get-xhr-server/$', views.get_xhr_server, name='get-xhr-server'),
    # user/register/
    url(r'^register/$', views.register, name='register'),
    # user/checkuname/
    url(r'^checkuname/$', views.checkuname, name='checkuname'),
    # user/makepost/
    url(r'^makepost/$', views.makepost, name='makepost'),
    # user/getuser/
    url(r'^getuser/$', views.get_user, name='getuser'),
    # user/getuserserver/
    url(r'^getuserserver/$', views.get_user_server, name='getuserserver'),
    # user/jsonobj/
    url(r'^jsonobj/$', views.json_obj, name="json_obj"),
    # user/jsondumps/
    url(r'^jsondumps/$', views.json_dumps, name="json_dumps"),
]
