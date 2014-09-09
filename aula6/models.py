from django.db import models

class Contact(models.Model):

	first_name = models.CharField(maxLenght=30)
	last_name = models.CharField(maxLenght=30)
	email = models.EmailField(maxLenght=50)
	twitter = models.URLField(maxLenght=200)

	def __unicode__(self):
		return