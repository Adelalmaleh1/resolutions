from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=30)
	organisation = models.CharField(max_length=100)
	content = models.TextField('Message', max_length=500)

	def __unicode__(self):
		return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title