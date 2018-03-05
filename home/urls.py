# -*- coding:utf-8 -*-
from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
]