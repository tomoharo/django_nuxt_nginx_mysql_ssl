# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from myapp import urls # myapp配下のurls.pyをimport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]
