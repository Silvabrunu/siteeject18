from django.shortcuts import render
from siteeject import forms

def sites_responsivos(request):
	context = {
		'form_responsivos': forms.SitesResponsivosForm()
	}

	if request.method == 'POST':
		form = forms.SitesResponsivosForm(request.POST)
		
		if form.is_valid():
			context['enviado'] = form.send_email(form.cleaned_data['origem'], form.cleaned_data['opcoes'])

	return render(request, 'sites-responsivos.html', context)

def sistemas_web(request):
	context = {
		'form_sistemas': forms.SistemasWebForm()
	}

	if request.method == 'POST':
		form = forms.SistemasWebForm(request.POST)

		if form.is_valid():
			context['enviado'] = form.send_email(form.cleaned_data['origem'], form.cleaned_data['opcoes'])

	return render(request, 'sistemas-web.html', context)

def hospedagem(request):
	context = {
		'form_hospedagem': forms.HospedagemForm()
	}

	if request.method == 'POST':
		form = forms.HospedagemForm(request.POST)

		if form.is_valid():
			context['enviado'] = form.send_email(form.cleaned_data['origem'], form.cleaned_data['opcoes'])

	return render(request, 'hospedagem.html', context)