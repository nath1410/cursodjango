# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
	lista = ['Nome 1', 'Nome 2', 'Nome 3']
	return render(request, 'aula4/index.html', {'nome': 'Teste', 'idade': 99, 'lista': lista})
