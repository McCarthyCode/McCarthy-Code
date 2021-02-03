from django.urls import re_path

from . import views
from mwd.settings import STAGE

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^portfolio/$', views.portfolio, name='portfolio'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    re_path(r'^sites/$', views.sites, name='sites'),
    re_path(r'^sites/reorder/$', views.reorder_sites, name='reorder-sites'),
    re_path(r'^sites/add/$', views.add_site, name='add-site'),
    re_path(r'^sites/(?P<site_id>[1-9]\d*)/edit/$', views.edit_site, name='edit-site'),
    re_path(r'^sites/(?P<site_id>[1-9]\d*)/delete/$', views.delete_site, name='delete-site'),
    re_path(r'^sites/(?P<site_id>[1-9]\d*)/delete-screenshot/(?P<screenshot_id>[1-9]\d*)/$', views.delete_screenshot, name='delete-screenshot'),
    re_path(r'^sites/(?P<site_id>[1-9]\d*)/delete-screenshots/$', views.delete_screenshots, name='delete-screenshots'),
]

if STAGE != 'production':
    urlpatterns += [
        re_path(r'^400/$', views.view_400),
        re_path(r'^403/$', views.view_403),
        re_path(r'^404/$', views.view_404),
        re_path(r'^500/$', views.view_500),
    ]
