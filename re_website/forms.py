from django import forms

from .models import Contact

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
