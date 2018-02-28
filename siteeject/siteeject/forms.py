from django import forms
from django.core.mail import EmailMessage

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