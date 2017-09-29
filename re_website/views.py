from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from .models import Contact
from .forms import ContactForm
from django.core.urlresolvers import reverse


__all__ = (
    'HomeTemplateView,'
    'ContactView,'
    'FinancialView,'
    'ValuerView,'
    'AnalysisView,'

    
)
class HomeTemplateView(TemplateView):
    template_name = 'home.html'   
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        return context
    def get(self, request):
        form = ContactForm()
        model = Contact
        context = {
            'form': form,
        }
        return render(request, 'home.html', context)


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

class FinancialView(TemplateView):
    template_name = 'financial.html'

class ValuerView(CreateView):
    template_name = 'valuer.html'
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
        return reverse('valuer')

class AnalysisView(TemplateView):
    template_name = 'analysis.html'
    
