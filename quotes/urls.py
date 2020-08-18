from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^manager/$', views.manager, name='manager'),
    re_path(r'^delete/(?P<quote_id>[1-9]\d*)/$', views.delete, name='delete'),
]
