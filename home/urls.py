from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^portfolio/$', views.portfolio, name='portfolio'),
    re_path(r'^portfolio/add/$', views.add_site, name='add-site'),
    re_path(r'^portfolio/edit/(?P<site_id>[1-9]\d*)/$', views.edit_site, name='edit-site'),
]
