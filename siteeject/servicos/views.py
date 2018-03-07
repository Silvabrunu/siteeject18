from django.shortcuts import render
from siteeject import forms

def sites_responsivos(request):
	context = {
		'form_responsivos': forms.SitesResponsivosForm()
	}

	return render(request, 'sites-responsivos.html', context)

def sistemas_web(request):
	context = {
		'form_sistemas': forms.SistemasWebForm()
	}

	return render(request, 'sistemas-web.html', context)

def hospedagem(request):
	context = {
		'form_hospedagem': forms.HospedagemForm()
	}

	return render(request, 'hospedagem.html', context)