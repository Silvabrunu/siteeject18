# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from .models import QuemSomos, Portifolio, Depoimentos, Parceiros
from siteeject import forms


def index(request):
	success = False
	form = forms.ContactSoliciteUmaProposta()
	formServicoResponsivo = forms.ContactServicoSitesResponsivos()
	formServicoSistemaWEB = forms.ContactServicoSistemasWEB()
	formServicoHospedagem = forms.ContactServicoHospedagem()


	if request.method == 'POST':
		validacaoProposta = request.POST.get("validacaoProposta")
		validacaoResponsivo = request.POST.get("validacaoServicoResponsivo")
		validacaoSistemaWEB = request.POST.get("validacaoServicoSistemaWEB")
		validacaoHospedagem = request.POST.get("validacaoServicoHospedagem")
		form = forms.ContactSoliciteUmaProposta(request.POST)
		slideTitulo = "HOME"
		
		if validacaoProposta == 'valido':
			if form.is_valid():
				lugar = "Solicite uma proposta"
				name = form.cleaned_data['name']
				about = form.cleaned_data['about']
				email = form.cleaned_data['email']
				phone = form.cleaned_data['phone']
				deviceContact = form.cleaned_data['deviceContact']
				subject = 'Contato sobre:{0} + {1} + {2}'.format(about, lugar, slideTitulo)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}\nForma de contato:{3}'.format(name, email, phone, deviceContact)
				form = forms.ContactSoliciteUmaProposta()
				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			form = forms.ContactSoliciteUmaProposta()

		formServicoResponsivo = forms.ContactServicoSitesResponsivos(request.POST)
		if validacaoResponsivo == 'valido':
			
			if formServicoResponsivo.is_valid():
				success = False

				lugar2 = "Servico + Site responsivo"
				name2 = formServicoResponsivo.cleaned_data['name']
				phone2 = formServicoResponsivo.cleaned_data['phone']
				email2 = formServicoResponsivo.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar2)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name2, email2, phone2)
				formServicoResponsivo = forms.ContactServicoSitesResponsivos()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoResponsivo = forms.ContactServicoSitesResponsivos()

		formServicoSistemaWEB = forms.ContactServicoSistemasWEB(request.POST)
		if validacaoSistemaWEB == 'valido':
			
			if formServicoSistemaWEB.is_valid():
				success = False

				lugar = "Servico + SistemasWEB"
				name = formServicoSistemaWEB.cleaned_data['name']
				phone = formServicoSistemaWEB.cleaned_data['phone']
				email = formServicoSistemaWEB.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name, email, phone)
				formServicoSistemaWEB = forms.ContactServicoSistemasWEB()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoSistemaWEB = forms.ContactServicoSitesResponsivos()

		formServicoHospedagem = forms.ContactServicoHospedagem(request.POST)
		if validacaoHospedagem == 'valido':
			
			if formServicoHospedagem.is_valid():
				success = False

				lugar = "Servico + Hospedagem"
				name = formServicoHospedagem.cleaned_data['name']
				phone = formServicoHospedagem.cleaned_data['phone']
				email = formServicoHospedagem.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name, email, phone)
				formServicoHospedagem = forms.ContactServicoHospedagem()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoHospedagem = forms.ContactServicoHospedagem()

		form_contato = forms.Contato(request.POST)

		if form_contato.is_valid():
			success = form_contato.send_email('FOOTER HOME')

	context = {
		'form_solicitacao': form,
		'form_servico_responsivo': formServicoResponsivo,
		'form_servico_sistema_web': formServicoSistemaWEB,
		'form_servico_hospedagem': formServicoHospedagem,
		'form_contato': forms.Contato(),
	 	'success': success,
	 	'quem_somos': QuemSomos.objects.all(),
		'portifolio': Portifolio.objects.all(),
		'depoimentos': Depoimentos.objects.all(),
		'parceiros': Parceiros.objects.all(),
	}

	return render(request, 'index.html', context)

def quem_somos(request):
	context = {
		'quem_somos': QuemSomos.objects.all(),
		'form_contato': forms.Contato()
	}

	if request.method == 'POST':
		# form = forms.CorreioForm(request.POST)
		# form.persistir()
		form_contato = forms.Contato(request.POST)

		if form_contato.is_valid():
			context['enviado'] = form_contato.send_email('FOOTER QUEM SOMOS')

	return render(request, 'quem-somos.html', context)