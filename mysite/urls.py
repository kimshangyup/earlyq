from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
]
