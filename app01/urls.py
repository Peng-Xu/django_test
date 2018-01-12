from django.conf.urls import url,include
from django.contrib import admin
from app01.views import index, login, logout, regist


urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^regist/$', regist, name='regist'),
]
