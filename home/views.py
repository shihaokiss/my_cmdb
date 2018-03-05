# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'home/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginPageView, self).get_context_data(**kwargs)
        return context
