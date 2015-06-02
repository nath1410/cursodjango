from django.db import models

class Contact(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	twitter = models.URLField(max_length=200)

	def __unicode__(self):
		return self.first_name