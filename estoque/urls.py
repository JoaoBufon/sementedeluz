from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include, path, URLPattern
from django import views
from . import views
from django.contrib.auth import views as auth_views
from estoque.views import CadastroView, AddHigieneView, AddAlimentoView, AddFuncionarioView, AddIntegranteView, AddRoupaCamaView, AddRoupaView, VerAlimentoView, VerFuncionarioView, VerHigieneView, VerIntegranteView, VerRoupaCamaView, VerRoupaView
from django.contrib.auth.decorators import login_required

app_name = 'estoque'
urlpatterns = [
    path ('language/', TemplateView.as_view (template_name ='language.html ')),
    path ('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path ('cadastro/', CadastroView.as_view(), name='cadastro'),
    
    
    path ('opcaocadastro/', TemplateView.as_view (template_name ='opcao-cadastro.html '), name='opcaocadastro'),
    path ('estoquecategorias/', TemplateView.as_view (template_name ='estoque_categorias.html '),name='estoquecategorias'),
    path ('opcaovercadastro/', TemplateView.as_view (template_name ='opcao_ver_cadastro.html '), name='opcaovercadastro'),
    path ('opcaoverestoque/', TemplateView.as_view (template_name ='opcao_ver_estoque.html '), name='opcaoverestoque'),
    path ('opcaopessoas/', TemplateView.as_view (template_name ='cadastro_pessoas.html '), name='opcaopessoas'),
    path ('categoriascadastro/', TemplateView.as_view (template_name ='categorias_cadastro.html '), name='categoriascadastro'),
    path ('opcao/', TemplateView.as_view (template_name ='opcao_ver_estoque.html '), name='opcao'),
    path ('opcaoestoque/', TemplateView.as_view (template_name ='opcao_estoque.html '), name='opcaoestoque'),
    
    path ('escolha/', login_required (TemplateView.as_view (template_name ='escolha.html ')), name='escolha'),
    
    path ('addalimento/', AddAlimentoView.as_view (), name='addalimento'),
    path ('addhigiene/', AddHigieneView.as_view(), name='addhigiene'),
    path ('addroupadecama/', AddRoupaCamaView.as_view (), name='addroupacama'),
    path ('addroupas/', AddRoupaView.as_view (), name='addroupa'),
    path ('cadastrofuncionarios/', AddFuncionarioView.as_view (), name='cadastrofuncionarios'),
    path ('cadastrointegrantes/', AddIntegranteView.as_view (), name='cadastrointegrantes'), 
    
    
    path ('vercomida/', VerAlimentoView.as_view (), name='veralimento'),
    path ('verfuncionarios/', VerFuncionarioView.as_view (), name='verfuncionario'),
    path ('verhigiene/', VerHigieneView.as_view (), name='verhigiene'),
    path ('verroupacama/', VerRoupaCamaView.as_view (), name='verroupacama'),
    path ('verroupa/', VerRoupaView.as_view (), name='verroupa'),
    path ('verintegrante/', VerIntegranteView.as_view (), name='verintegrante'),
    
    #path('higiene/<int:pk>', )
    
    # nova url path ('/home', view),
    
    #pedir o que botar depois de views

]
