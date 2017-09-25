from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(max_length=30)
	organisation = models.CharField(max_length=100)
	content = models.TextField('Message', max_length=500)

	def __unicode__(self):
		return self.name