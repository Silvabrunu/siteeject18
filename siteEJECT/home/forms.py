# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.mail import send_mail
from django.conf import settings 



class ContactSoliciteUmaProposta(forms.Form):
	ABOUT_CHOICES = (
		("Selecione o serviço desejado", "Selecione o serviço desejado"),
		("Sites responsivos", "Sites Responsivos"),
		("Sistema Web", "Sistema Web"),
		("Hospedagem de Dados", "Hospedagem de Dados"),
	)

	DEVICE_CHOICES = (
		("Email", "Email"),
		("Telefone", "Telefone"),
		("Whatsapp", "Whatsapp"),
	)

	about = forms.ChoiceField(choices=ABOUT_CHOICES)
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label = 'Email')
	phone = forms.CharField(label = 'Telefone',max_length=15)
	deviceContact = forms.ChoiceField(choices= DEVICE_CHOICES, widget=forms.RadioSelect())
	#slide = forms.CharField(label='Slide', max_length=100, widget=forms.HiddenInput())
	#validacao = forms.CharField(label='validacao', widget=forms.HiddenInput())
	# message = forms.CharField(label='Mensagem', widget=forms.Textarea)


class ContactServicoSitesResponsivos(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label = 'Email')
	phone = forms.CharField(label = 'Telefone',max_length=15)
	#validacao = forms.CharField(label='Validacao', widget=forms.HiddenInput())
	# message = forms.CharField(label='Mensagem', widget=forms.Textarea)

class ContactServicoSistemasWEB(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label = 'Email')
	phone = forms.CharField(label = 'Telefone',max_length=15)

class ContactServicoHospedagem(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label = 'Email')
	phone = forms.CharField(label = 'Telefone',max_length=15)
