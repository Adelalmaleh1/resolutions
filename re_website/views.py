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
        context = {
            'blog_list' : blogs, 
        }
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

class ValuerView(TemplateView):
    template_name = 'valuer.html'

class AnalysisView(TemplateView):
    template_name = 'analysis.html'
    
