from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^delete/(?P<pk>\d+)/$', views.delete),
    url(r'^write/$', views.write),
]