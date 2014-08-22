# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class contato(models.Model):
	
	nome = models.CharField(max_length=100)
	email = models.EmailField()
	twitter = models.URLField()