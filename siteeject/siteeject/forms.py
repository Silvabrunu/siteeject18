# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import EmailMessage
from siteeject import settings
from core.models import Correio

class Contato(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome', 'id': 'nome'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Telefone', 'id': 'phone'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor Email', 'id': 'email'}))
    assunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto', 'id': 'subject'}))
    mensagem = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'id': 'message', 'rows': '6'}))

    def send_email(self, origem):
        subject = self.cleaned_data['assunto']
        message = \
            """
            <table>
                <tr>
                    <th>Nome: </th>
                    <td>""" + self.cleaned_data['nome'] + """</td>
                </tr>
                <tr>
                    <th>Telefone: </th>
                    <td>""" + self.cleaned_data['telefone'] + """</td>
                </tr>
                <tr>
                    <th>E-mail: </th>
                    <td>""" + self.cleaned_data['email'] + """</td>
                </tr>
                <tr>
                    <th>Mensagem: </th>
                    <td>""" + self.cleaned_data['mensagem'] + """</td>
                </tr>
                <tr>
                    <th>Local do formulário: </th>
                    <td>""" + origem + """</td>
                </tr>
            </table>
            """

        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
        email.content_subtype = "html"
        try:
            email.send()
        except Exception:
            return  False

        return True

class CorreioForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome', 'id': 'nome'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor Email', 'id': 'email'}))
    empresa = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa', 'id': 'empresa'}))

    def persistir(self):
        if self.is_valid():
            try:
                correio = Correio()

                correio.nome = self.cleaned_data['nome']
                correio.email = self.cleaned_data['email']
                correio.empresa = self.cleaned_data['empresa']

                correio.save()
            except Exception:
                return False

        return True

class Servicos(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'r-form-first-name form-control', 'placeholder': 'Seu Nome', 'id': 'nome'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'id': 'telefone', 'data-mask': '(00) 00000-0000'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor Email', 'id': 'email'}))

    def send_email(self, origem, opcoes):
        subject = "Solicitação de Orçamento"
        message = \
            """
            <table>
                <tr>
                    <th>Nome: </th>
                    <td>""" + self.cleaned_data['nome'] + """</td>
                </tr>
                <tr>
                    <th>Telefone: </th>
                    <td>""" + self.cleaned_data['telefone'] + """</td>
                </tr>
                <tr>
                    <th>E-mail: </th>
                    <td>""" + self.cleaned_data['email'] + """</td>
                </tr>
                <tr>
                    <th>Produto: </th>
                    <td>""" + opcoes + """</td>
                </tr>
                <tr>
                    <th>Local do formulário: </th>
                    <td>""" + origem + """</td>
                </tr>
            </table>
            """
        
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
        email.content_subtype = "html"

        try:
            email.send()
        except Exception:
            return  False

        return True


class SitesResponsivosForm(Servicos):
    CHOICES = (
        ('0', 'Qual o site que te interessa?'),
        ('INSTITUCIONAIS', 'Institucionais'),
        ('BLOG', 'Blog'),
        ('E-COMMERCE', 'E-Commerce'),
        ('LANDING PAGE', 'Landing Page'),
        ('OUTRO TIPO', 'Outro Tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))
    origem = forms.CharField(max_length=100, widget=forms.HiddenInput(attrs={'value': 'SITES RESPONSIVOS'}))

class SistemasWebForm(Servicos):
    CHOICES = (
        ('0', 'Qual o sistema que te interessa?'),
        ('GESTÃO INTERNA', 'Gestão Interna'),
        ('CRM', 'CRM'),
        ('MVP', 'MVP'),
        ('CONTROLE DE EVENTOS', 'Controle de Eventos'),
        ('OUTRO TIPO', 'Outro Tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))
    origem = forms.CharField(max_length=100, widget=forms.HiddenInput(attrs={'value': 'SISTEMAS WEB'}))

class HospedagemForm(Servicos):
    CHOICES = (
        ('0', 'O que te interessa?'),
        ('PLANO DE HOSPEDAGEM', 'Plano Anual de Hospedagem'),
        ('E-MAIL PROFISSIONAL', 'E-mails Profissionais'),
        ('OUTRO TIPO', 'Outro tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))
    origem = forms.CharField(max_length=100, widget=forms.HiddenInput(attrs={'value': 'HOSPEDAGEM'}))

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

    about = forms.ChoiceField(choices=ABOUT_CHOICES, widget=forms.Select(attrs={'class': 'form-control selectpicker', 'id': 'about'}))
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Nome e Sobrenome', 'id': 'name', 'required': 'required'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'form-control input-lg', 'placeholder': 'E-mail', 'id': 'email', 'required': 'required'}))
    phone = forms.CharField(label = 'Telefone',max_length=15, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Telefone', 'id': 'phone', 'required': 'required'}))
    deviceContact = forms.ChoiceField(choices= DEVICE_CHOICES, widget=forms.RadioSelect())


class ContactServicoSitesResponsivos(forms.Form):

    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'control-name', 'placeholder': 'Seu Nome'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'control-email', 'placeholder': 'E-mail'}))
    phone = forms.CharField(label = 'Telefone',max_length=15, widget=forms.EmailInput(attrs={'class': 'control-phone', 'placeholder': 'Telefone'}))

class ContactServicoSistemasWEB(forms.Form):

    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'control-name', 'placeholder': 'Seu Nome'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'control-email', 'placeholder': 'E-mail'}))
    phone = forms.CharField(label = 'Telefone',max_length=15, widget=forms.EmailInput(attrs={'class': 'control-phone', 'placeholder': 'Telefone'}))

class ContactServicoHospedagem(forms.Form):

    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'control-name', 'placeholder': 'Seu Nome'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'control-email', 'placeholder': 'E-mail'}))
    phone = forms.CharField(label = 'Telefone',max_length=15, widget=forms.EmailInput(attrs={'class': 'control-phone', 'placeholder': 'Telefone'}))