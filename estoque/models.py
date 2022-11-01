from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

HIGIENE_CHOICES = (
        ('Sabonete', 'Sabonete'),
        ('Escoava de dentes', 'Escova de dentes'),
        ('Pasta de dentes', 'Pasta de dentes'),
        ('Papel Higiênico', 'Papel Higiênico'),
    )
ROUPA_CHOICES = (
        ('1', 'Calça'),
        ('2', 'Casaco'),
        ('3', 'Camiseta'),
        ('4', 'Camisa'),
    )
ALIMENTO_CHOICES = (
        ('1', 'Carboidrato'),
        ('2', 'sei la'),
        ('3', 'Pasta de dentes'),
        ('4', 'Papel Higiênico'),
    )
ROUPACAMA_CHOICES = (
        ('1', 'Lençol'),
        ('2', 'Cobertor'),
        ('3', 'Fronha'),
        ('4', 'sei la'),
    )
TAMANHOROUPACAMA_CHOICES = (
        ('Solteiro', 'Solteiro'),
        ('Casal', 'Casal'),
        ('QueenSize', 'QueenSize'),
        ('KingSize', 'KingSize'),
    )
TAMANHOROUPA_CHOICES = (
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    )
CONDICAO_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

SEXO_CHOICES = (
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino'),
)

class Cadastro(models.Model):
    nome=models.CharField(max_length = 100, null=True)
    sobrenome=models.CharField(max_length = 100, null=True)
    email=models.EmailField(null=True)
    telefone = models.CharField(max_length = 12, null=True)
    senha = models.CharField(max_length = 30, null=True)
    
    def __str__(self):
        return self.nome
 

class Integrante(models.Model):
    nome=models.CharField(max_length = 100, null=True)
    email=models.EmailField(null=True)
    telefone = models.CharField(max_length = 12, null=True)
    dt_ingresso=models.DateField(null=True)
    dt_nasct=models.DateField(null=True)
    cpf = models.CharField(max_length = 11, null=True)
    
    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome=models.CharField(max_length = 100, null=True)
    email=models.EmailField(null=True)
    dt_ingresso=models.DateField(null=True)
    dt_nasct=models.DateField(null=True)
    cpf = models.CharField(max_length = 11, null=True)
    telefone = models.CharField(max_length = 12, null=True)
    cep = models.CharField(max_length=15, null=True)
    endereco = models.CharField(max_length=50, null=True)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES, null=True)
    
    def __str__(self):
        return self.nome
    
class Roupa (models.Model):
    tipos = models.CharField (max_length = 30, choices=ROUPA_CHOICES, null=True)
    cor = models.CharField (max_length = 30, null=True)
    qntd = models.IntegerField(null=True)
    tamanho = models.CharField(max_length = 3, choices=TAMANHOROUPA_CHOICES, null=True)
    condicao = models.IntegerField(choices=CONDICAO_CHOICES, null=True)
    
    def __str__(self):
        return self.tipos
    
class Alimento (models.Model):
    tipos = models.CharField (max_length=30, choices=ALIMENTO_CHOICES, null=True)
    descr = models.CharField (max_length=30, null=True)
    qntd = models.FloatField(null=True)
    vencimento = models.DateField(null=True)
    
    def __str__(self):
        return self.descr
    

class Higiene (models.Model):
    tipos = models.CharField (max_length=30, choices=HIGIENE_CHOICES, null=True)
    descr = models.CharField(max_length=30, null=True)
    qntd = models.IntegerField(null=True)
    vencimento = models.DateField(null=True)
    
    def __str__(self):
        return self.descr

class Roupacama (models.Model):
    
    tipos = models.CharField (max_length = 30, choices=ROUPACAMA_CHOICES, null=True)
    descr = models.CharField (max_length=30, null=True)
    cor = models.CharField (max_length = 30, null=True)
    qntd = models.IntegerField(null=True)
    tamanho = models.CharField(max_length = 10, choices=TAMANHOROUPACAMA_CHOICES, null=True)
    condicao = models.IntegerField(choices=CONDICAO_CHOICES, null=True)
    
    def __str__(self):
        return self.descr
    