import datetime
from email.policy import default
from django.db import models
#?data e horario atual
from django.utils import timezone

# Create your models here.
lista_categorias = (
    #? (como vai armazenar no BD, "aparecer pro cliente")
    ("ANALISE" ,  "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)
#! TABELAS
#? criar filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=100,)
    thumb = models.ImageField(upload_to="thumb_filmes")
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=lista_categorias)
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    #? definir nome da classe ao imprimir
    def __str__(self):
        return self.titulo


#? criar os epsodios

#? criar usuário