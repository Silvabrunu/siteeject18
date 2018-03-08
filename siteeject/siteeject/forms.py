# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import EmailMessage
from core.models import Correio

class Contato(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome', 'id': 'nome'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Telefone', 'id': 'phone'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor Email', 'id': 'email'}))
    assunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto', 'id': 'subject'}))
    mensagem = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'id': 'message', 'rows': '6'}))
    origem = forms.CharField(max_length=100, widget=forms.HiddenInput(attrs={'value': 'FOOTER'}))

    def send_email(self):
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
                    <td>""" + self.cleaned_data['origem'] + """</td>
                </tr>
            </table>
            """

        email = EmailMessage(subject, message, 'periclesgdc@gmail.com', ['periclesgdc@hotmail.com'])
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

    def send_email(self, origem, opcao):
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
                    <td>""" + opcao + """</td>
                </tr>
                <tr>
                    <th>Local do formulário: </th>
                    <td>""" + origem + """</td>
                </tr>
            </table>
            """
        
        email = EmailMessage(subject, message, 'periclesgdc@gmail.com', ['periclesgdc@hotmail.com'])
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
