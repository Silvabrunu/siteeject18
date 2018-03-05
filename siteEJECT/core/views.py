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
	
	if request.method == 'POST':
		
		form = ContactSoliciteUmaProposta(request.POST)
		if form.is_valid():
			success = False
			# context={'is_valid':True}
			# form.send_mail()
			lugar = "Solicite uma proposta"
			name = form.cleaned_data['name']
			about = form.cleaned_data['about']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			deviceContact = form.cleaned_data['deviceContact']
			slide = form.cleaned_data['slide']
			subject = 'Contato sobre:{0} + {1} + {2}'.format(about, lugar, slide)
			message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}\nForma de contato:{3}'.format(name, email, phone, deviceContact)
			form = ContactSoliciteUmaProposta()

			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
			success = True

		form2 = ContactServicoSitesResponsivos(request.POST)
		if form2.is_valid():
			success = False

			lugar2 = "Site responsivo"
			name2 = form2.cleaned_data['name']
			phone2 = form2.cleaned_data['phone']
			email2 = form2.cleaned_data['email']
		
			subject = 'Contato sobre: Nossos servicos + {0}'.format(lugar2)
			message = 'Nome: {0}\nE-mail:{1}\nTelefone:{2}'.format(name2, email2, phone2)
			form2 = ContactServicoSitesResponsivos()

			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
			success = True
	else:
		form = ContactSoliciteUmaProposta()
		form2 = ContactServicoSitesResponsivos()

	context = {
		'banner': SlideShow.objects.all(), 
		'partner': Partner.objects.all(),
	 	'form':form,
	 	'form2':form2,
	 	'success':success,

	}
	return render(request, 'index.html', context)