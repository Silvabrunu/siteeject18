from django.shortcuts import render
from .models import QuemSomos, Portifolio, Depoimentos, Parceiros

def index(request):
	
	context = {
		'quem_somos': QuemSomos.objects.all(),
		'portifolio': Portifolio.objects.all(),
		'depoimentos': Depoimentos.objects.all(),
		'parceiros': Parceiros.objects.all()
	}

	return render(request, 'index.html', context)