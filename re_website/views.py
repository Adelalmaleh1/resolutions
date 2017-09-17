from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
        return context
        