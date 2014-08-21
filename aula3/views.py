# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == 'POST':
		nome = request.POST.get('name', 'não tem nome')
		return HttpResponse('O nome é %s' % nome)
	else:
		formulario = '''
		<form action="." method="post">
		<input type="text" name="name" maxlenght="100" />
		<button type="submit">Enviar</button>
		</form>
		'''
		return HttpResponse(formulario)


def detail(request, username):
	return HttpResponse('O username é: %s' % username) 