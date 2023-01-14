from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('fakenews', views.fakenews, name='fakenews'),
    path('summary', views.summary, name='summary'),
    path('pressnpulse', views.pressnpulse, name='pressnpulse'),
    path('usingname', views.usingname, name='usingname'),
    path('usingurl', views.usingurl, name='usingurl'),
    path('usingimage', views.usingimage, name='usingimage'),
    path('about', views.about, name='about')
]
