"""runconde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
    url(r'^news-index/$',views.news_index, name = 'news-index'),
    url(r'^news-index/(?P<pk>\d+)/',views.news_detail, name = 'news-detail'),
    url(r'^blog-index/$',views.blog_index, name = 'blog-index'),
    url(r'^blog-index/(?P<pk>\d+)/',views.blog_detail, name = 'blog-detail'),
    url(r'^share-index/',views.share_index, name = 'share-index'),
    url(r'^register/',views.register, name = 'register'),
    url(r'^login/',views.login, name = 'login'),
    url(r'^logout/',views.logout, name = 'logout'),
    url(r'^tag/(?P<tag>\S+)/',views.tag, name = 'tag'),
    url(r'^userinfo/', views.userinfo, name='userinfo'),
	url(r'^ueditor/',include(DjangoUeditor_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_check_username/',views.ajax_check_username, name = 'ajax_check-username'),
    url(r'^ajax_feedback/',views.ajax_feedback, name = 'ajax_feedback')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
