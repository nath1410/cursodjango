from django.shortcuts import render
from django.http import HttpResponse
from aula6.models import Contact


def index(request):
	contatos = Contact.objects.all()

	if request.method == 'POST':
		nome = request.POST.get('first_name')
		sobrenome = request.POST.get('last_name')
		email = request.POST.get('email')
		twitter = request.POST.get('twitter')
		novo_contato = Contact(
			first_name=nome,
			last_name=sobrenome,
			email=email,
			twitter=twitter
		)
		novo_contato.save()

	return render(request, 'aula6/index.html',
		{
			'contatos': contatos,
		}
	)