from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/add/', views.add_site, name='add-site'),
]
