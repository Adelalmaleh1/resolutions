from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from .models import Contact
from django.core.urlresolvers import reverse


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
        return context


class ContactView(CreateView):
    template_name = 'contact.html'
    form = ContactForm()
    fields = (
        'name',
        'email',
        'phone',
        'organisation',
        'content',
        )
    model = Contact
    def get_success_url(self):
        return reverse('contact')
    
