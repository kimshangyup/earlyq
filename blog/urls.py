from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', views.channel_list),
    url(r'^channel/(?P<channel_pk>\w+)/$', views.question_list),
    url(r'^create/$', views.channel_create),
    url(r'^delete/(?P<pk>\d+)/$', views.channel_delete),
    url(r'^search/$', views.search),
    url(r'^remove/(?P<pk>\d+)/$', views.delete),
    url(r'^write/$', views.write),
]