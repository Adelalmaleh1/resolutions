from django import forms

from .models import Contact, Blog

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'organisation', 'content']

        required = {
            'name': True,
            'email': True,
            'phone': True,
            'organisation': True,
            'content': True
            }
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
                'title', 
                'text',
                'created_date'
                ]
        required = {
            'title': True,
            'text': True,
        }

