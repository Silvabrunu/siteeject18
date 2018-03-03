from django.shortcuts import render
from .models import QuemSomos, Portifolio, Depoimentos, Parceiros
from siteeject import forms


def index(request):
    context = {
        'quem_somos': QuemSomos.objects.all(),
        'portifolio': Portifolio.objects.all(),
        'depoimentos': Depoimentos.objects.all(),
        'parceiros': Parceiros.objects.all(),
        'form_contato': forms.Contato()
    }

    if request.method == 'POST':
        form = forms.Contato(request.POST)

        if form.is_valid():
            context['enviado'] = form.send_email()

    return render(request, 'index.html', context)

def quem_somos(request):
    context = {
        'quem_somos': QuemSomos.objects.all()
    }

    return render(request, 'quem-somos.html', context)