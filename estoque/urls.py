from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include, path, URLPattern
from django import views
from . import views
from django.contrib.auth import views as auth_views
from estoque.views import logoutUser, loginPage, CadastroView, AddHigieneView, AddAlimentoView, AddFuncionarioView, AddIntegranteView, AddRoupaCamaView, AddRoupaView, VerAlimentoView, VerFuncionarioView, VerHigieneView, VerIntegranteView, VerRoupaCamaView, VerRoupaView
from django.contrib.auth.decorators import login_required

app_name = 'estoque'
urlpatterns = [
    path ('language/', TemplateView.as_view (template_name ='language.html ')),
    path ('login/', views.loginPage, name='login'),
    path ('cadastro/', views.CadastroView, name='cadastro'),
    path ('logout/', views.logoutUser, name='logout'),
    
    path ('opcaocadastro/', login_required (TemplateView.as_view (template_name ='opcao-cadastro.html ')), name='opcaocadastro'),
    path ('estoquecategorias/', login_required (TemplateView.as_view (template_name ='estoque_categorias.html ')),name='estoquecategorias'),
    path ('opcaovercadastro/', login_required (TemplateView.as_view (template_name ='opcao_ver_cadastro.html ')), name='opcaovercadastro'),
    path ('opcaoverestoque/', login_required (TemplateView.as_view (template_name ='opcao_ver_estoque.html ')), name='opcaoverestoque'),
    path ('opcaopessoas/', login_required (TemplateView.as_view (template_name ='cadastro_pessoas.html ')), name='opcaopessoas'),
    path ('categoriascadastro/', login_required (TemplateView.as_view (template_name ='categorias_cadastro.html ')), name='categoriascadastro'),
    path ('opcao/', login_required (TemplateView.as_view (template_name ='opcao_ver_estoque.html ')), name='opcao'),
    path ('opcaoestoque/', login_required (TemplateView.as_view (template_name ='opcao_estoque.html ')), name='opcaoestoque'),
    
    path ('escolha/', login_required (TemplateView.as_view (template_name ='escolha.html ')), name='escolha'),
    
    path ('addalimento/', login_required (AddAlimentoView.as_view ()), name='addalimento'),
    path ('addhigiene/', login_required (AddHigieneView.as_view()), name='addhigiene'),
    path ('addroupadecama/', login_required (AddRoupaCamaView.as_view ()), name='addroupacama'),
    path ('addroupas/', login_required (AddRoupaView.as_view ()), name='addroupa'),
    path ('cadastrofuncionarios/', login_required(AddFuncionarioView.as_view ()), name='cadastrofuncionarios'),
    path ('cadastrointegrantes/', login_required (AddIntegranteView.as_view ()), name='cadastrointegrantes'), 
    
    
    path ('vercomida/', login_required (VerAlimentoView.as_view ()), name='veralimento'),
    path ('verfuncionarios/', login_required (VerFuncionarioView.as_view ()), name='verfuncionario'),
    path ('verhigiene/', login_required (VerHigieneView.as_view ()), name='verhigiene'),
    path ('verroupacama/', login_required (VerRoupaCamaView.as_view ()), name='verroupacama'),
    path ('verroupa/', login_required (VerRoupaView.as_view ()), name='verroupa'),
    path ('verintegrante/', login_required (VerIntegranteView.as_view ()), name='verintegrante'),
    
    
    path ('perfil/', login_required (TemplateView.as_view (template_name ='perfil.html ')), name='perfil'),
    #path('higiene/<int:pk>', )
    
    # nova url path ('/home', view),
    
    #pedir o que botar depois de views

]
