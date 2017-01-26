from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', 'blog.views.test'),
    url(r'^yoonzi$', 'blog.views.yoonzi'),
    url(r'^yoonzi1$', 'blog.views.yoonzi1'),
    url(r'^yoonzi2$', 'blog.views.yoonzi2'),
    url(r'^yoonzi3$', 'blog.views.yoonzi3'),
    url(r'^yoonzi4$', 'blog.views.yoonzi4'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
]
