from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', 'blog.views.index'),
    url(r'^test/$', 'blog.views.test'),
    url(r'^email/$', 'blog.views.email'),
]
