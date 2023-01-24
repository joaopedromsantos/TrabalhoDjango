from django.db import models
from Estagio.models import Estagio

class Aluno(models.Model):
    ra = models.IntegerField(primary_key=True, editable=True)
    nome = models.CharField(max_length=45)
    ano_nascimento = models.IntegerField()
    cpf = models.CharField(max_length=14)
    cidade = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    rua = models.CharField(max_length=45)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, blank=True, null=True)

    #CHAVE ESTRANGEIRA#
    Estagio_id = models.ForeignKey(Estagio, on_delete=models.CASCADE, blank=True, null=True)



