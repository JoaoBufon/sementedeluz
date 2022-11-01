#from msilib.schema import ListView
from turtle import home
from django.shortcuts import render
from estoque.models import Cadastro, Funcionario
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from estoque.forms import ContactForm
from estoque.models import Alimento, Higiene, Integrante, Roupa, Roupacama, Integrante, Funcionario
from django.urls import reverse_lazy
    
class CadastroView(CreateView):
    model = Cadastro
    fields = '__all__'
    template_name = 'cadastro.html'
    #success_url = reverse_lazy('home')

'''
class loginView(FormView):
    model = Login
    template_name = 'login.html'
    
class homeView(FormView):
    model = Home
    template_name = 'home.html'
'''
class AddRoupaView(CreateView): 
    model = Roupa
    fields = ['tipos', 'cor', 'qntd', 'tamanho', 'condicao']
    template_name = 'add_roupas.html'
    
class AddRoupaCamaView(CreateView):
    model = Roupacama
    fields = ['tipos', 'descr', 'cor','qntd', 'tamanho', 'condicao']
    template_name = 'add_roupacama.html'
    
class AddHigieneView(CreateView):
    model = Higiene
    fields = ['tipos', 'descr', 'qntd', 'vencimento']
    template_name = 'add_higiene.html'
    success_url = '' # url
    
    def get_success_url(self) -> str:
        
        return super().get_success_url()
    
class HigieneDetail(DetailView):
    pass

class AddAlimentoView(CreateView):
    model = Alimento
    fields = ['tipos', 'descr', 'qntd', 'vencimento']
    template_name = 'add_comida.html'
       
class VerRoupaView(ListView):
    model= Roupa
    template_name = 'ver_roupas.html'
    
class VerRoupaCamaView(ListView):
    model= Roupacama
    template_name = 'ver_roupacama.html'
    
class VerHigieneView(ListView):
    model= Higiene
    template_name = 'ver_higiene.html'
    
class VerAlimentoView(ListView):
    model= Alimento
    template_name = 'ver_comida.html'

class VerIntegranteView(ListView):
    model= Integrante
    template_name = 'ver_visitantes.html'

class AddIntegranteView(CreateView):
    model = Integrante
    fields = ['nome', 'email', 'telefone', 'dt_ingresso','dt_nasct','cpf']
    template_name = 'add_visitantes.html'

class VerFuncionarioView(ListView):
    model= Funcionario
    template_name = 'ver_funcionarios.html'

class AddFuncionarioView(CreateView):
    model = Funcionario
    fields = ['nome', 'email', 'dt_ingresso', 'dt_nasct','cpf','telefone','cep','endereco','sexo']
    template_name = 'add_funcionarios.html'

    