# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	response = HttpResponse()
	response.write('Olá Mundo!')
	return response