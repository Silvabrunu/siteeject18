# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings 

from home.models import *
from home.forms import *

from django.http import HttpResponse

def index(request):
	success = False
	form = ContactSoliciteUmaProposta()
	formServicoResponsivo = ContactServicoSitesResponsivos()
	formServicoSistemaWEB = ContactServicoSistemasWEB()
	formServicoHospedagem = ContactServicoHospedagem()
	

	if request.method == 'POST':
		validacaoProposta = request.POST.get("validacaoProposta")
		validacaoResponsivo = request.POST.get("validacaoServicoResponsivo")
		validacaoSistemaWEB = request.POST.get("validacaoServicoSistemaWEB")
		validacaoHospedagem = request.POST.get("validacaoServicoHospedagem")
		form = ContactSoliciteUmaProposta(request.POST)
		slideTitulo = request.POST.get("tituloSlide")
		if validacaoProposta == 'valido':
		
			
			if form.is_valid():
				# context={'is_valid':True}
				# form.send_mail()
				lugar = "Solicite uma proposta"
				name = form.cleaned_data['name']
				about = form.cleaned_data['about']
				email = form.cleaned_data['email']
				phone = form.cleaned_data['phone']
				deviceContact = form.cleaned_data['deviceContact']
				#slide = form.cleaned_data['slide']
				subject = 'Contato sobre:{0} + {1} + {2}'.format(about, lugar, slideTitulo)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}\nForma de contato:{3}'.format(name, email, phone, deviceContact)
				form = ContactSoliciteUmaProposta()
				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			form = ContactSoliciteUmaProposta()

		formServicoResponsivo = ContactServicoSitesResponsivos(request.POST)
		if validacaoResponsivo == 'valido':
			
			if formServicoResponsivo.is_valid():
				success = False

				lugar2 = "Servico + Site responsivo"
				name2 = formServicoResponsivo.cleaned_data['name']
				phone2 = formServicoResponsivo.cleaned_data['phone']
				email2 = formServicoResponsivo.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar2)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name2, email2, phone2)
				formServicoResponsivo = ContactServicoSitesResponsivos()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoResponsivo = ContactServicoSitesResponsivos()

		formServicoSistemaWEB = ContactServicoSistemasWEB(request.POST)
		if validacaoSistemaWEB == 'valido':
			
			if formServicoSistemaWEB.is_valid():
				success = False

				lugar = "Servico + SistemasWEB"
				name = formServicoSistemaWEB.cleaned_data['name']
				phone = formServicoSistemaWEB.cleaned_data['phone']
				email = formServicoSistemaWEB.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name, email, phone)
				formServicoSistemaWEB = ContactServicoSistemasWEB()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoSistemaWEB = ContactServicoSitesResponsivos()

		formServicoHospedagem = ContactServicoHospedagem(request.POST)
		if validacaoHospedagem == 'valido':
			
			if formServicoHospedagem.is_valid():
				success = False

				lugar = "Servico + Hospedagem"
				name = formServicoHospedagem.cleaned_data['name']
				phone = formServicoHospedagem.cleaned_data['phone']
				email = formServicoHospedagem.cleaned_data['email']
		
				subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar)
				message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name, email, phone)
				formServicoHospedagem = ContactServicoHospedagem()

				send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
				success = True
		else:
			formServicoHospedagem = ContactServicoHospedagem()

	context = {
		'banner': SlideShow.objects.all(), 
		'partner': Partner.objects.all(),
		'form':form,
		'form2':formServicoResponsivo,
		'form3':formServicoSistemaWEB,
		'form4':formServicoHospedagem,
	 	'success':success,

	}
	return render(request, 'index.html', context)