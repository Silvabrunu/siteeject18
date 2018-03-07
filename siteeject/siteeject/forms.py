from django import forms
from django.core.mail import EmailMessage
from core.models import Correio

class Contato(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome', 'id': 'nome'}))
    telefone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Telefone', 'id': 'phone'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor Email', 'id': 'email'}))
    assunto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto', 'id': 'subject'}))
    mensagem = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'id': 'message', 'rows': '6'}))

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
                    <td>FOOTER</td>
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

class SitesResponsivosForm(Servicos):
    CHOICES = (
        ('1', 'Qual o site que te interessa?'),
        ('2', 'Institucionais'),
        ('3', 'Blog'),
        ('4', 'E-Commerce'),
        ('5', 'Landing Page'),
        ('6', 'Outro Tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))

class SistemasWebForm(Servicos):
    CHOICES = (
        ('1', 'Qual o sistema que te interessa?'),
        ('2', 'Gestão Interna'),
        ('3', 'CRM'),
        ('4', 'MVP'),
        ('5', 'Controle de Eventos'),
        ('6', 'Outro Tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))

class HospedagemForm(Servicos):
    CHOICES = (
        ('1', 'O que te interessa?'),
        ('2', 'Plano Anual de Hospedagem'),
        ('3', 'E-mails Profissionais'),
        ('4', 'Outro tipo')
    )

    opcoes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'basic'}))
