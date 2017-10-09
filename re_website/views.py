from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView
from .models import Contact, Blog
from .forms import ContactForm, BlogForm
from django.core.urlresolvers import reverse


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
        'organization',
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
        'organization',
        'content',
        )
    model = Contact
    def get_success_url(self):
        return reverse('valuer')

class AnalysisView(TemplateView):
    template_name = 'analysis.html'
    
class DataView(TemplateView):
    template_name = 'data.html'

class BlogCreateView(CreateView):
    template_name = 'create_blog.html'
    model = Blog
    fields = ('title', 'text')
    def get_success_url(self):
        return reverse('blog')

def blog_list(request):
    blog_list = Blog.objects.all().order_by('-created_date') 
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'blogs': blog})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_details.html'