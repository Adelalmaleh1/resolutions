"""resolutions URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from re_website.views import HomeTemplateView, ContactView, FinancialView, ValuerView, AnalysisView,DataView, blog_list, BlogCreateView

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),

    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^financial/$', FinancialView.as_view(), name='financial'),
    url(r'^valuer/$', ValuerView.as_view(), name='valuer'),
    url(r'^analysis/$', AnalysisView.as_view(), name='analysis'),
    url(r'^data/$', DataView.as_view(), name='data'),
    url(r'^blog/$', blog_list, name='blog'),
    url(r'^blog/new/$', BlogCreateView.as_view(), name='blog_new'),
    url(r'^admin/', admin.site.urls),
]
