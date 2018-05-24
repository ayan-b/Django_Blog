"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as account_views
from boards import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^forum/boards/(?P<pk>\d+)/$', views.board_topics, name = 'board_topics'),
    url(r'^forum/boards/(?P<pk>\d+)/new/$', views.new_topic, name = 'new_topic'),
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^forum/', views.home, name = 'home'),

]
