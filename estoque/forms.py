from django import forms
from django.forms import ModelForm
from estoque.models import Cadastro
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length = 100)
    sobrenome = forms.CharField(max_length = 100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length = 12)
    senha = forms.CharField(max_length = 30)

class IntegranteForm(forms.Form):
    nome=forms.CharField(max_length = 100)
    sobrenome=forms.CharField(max_length = 100)
    telefone = forms.CharField(max_length = 12)
    cpf = forms.CharField(max_length = 11)

class RoupaForm (forms.Form):
    cor = forms.CharField (max_length = 30)
    qntd = forms.IntegerField()
    tamanho = forms.CharField(max_length = 3)
    descr = forms.CharField (max_length = 300)
    condicao = forms.IntegerField()
    
class Alimento (forms.Form):
    qntd = forms.FloatField()
    vencimento = forms.DateField()
    descr = forms.CharField (max_length = 300)
    
class Higiene (forms.Form):
    descr = forms.CharField (max_length = 300)
    qntd = forms.IntegerField()
    vencimento = forms.DateField()
    condicao = forms.IntegerField()

class Roupacama (forms.Form):
    qntd = forms.IntegerField()
    tamanho = forms.CharField(max_length = 10)
    descr = forms.CharField (max_length = 300)
    