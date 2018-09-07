from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from . import views

def test(request):
    return HttpResponse('This is app lvl')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process)
]