from uuid import uuid1

from django.db import models

class Disciplina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome = models.CharField(max_length=45)
    conteudo = models.CharField(max_length=300)
    carga_horaria = models.IntegerField()