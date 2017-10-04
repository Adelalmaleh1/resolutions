from django.contrib import admin
from .models import Contact, Blog

# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	class Meta:
		model = Contact


class BlogModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'created_date')
	class Meta:
		model = Blog

admin.site.register(Contact, ContactModelAdmin)

admin.site.register(Blog, BlogModelAdmin)