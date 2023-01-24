from uuid import uuid1

from django.db import models
from Aluno.models import Aluno
from Disciplina.models import Disciplina

class Matricula(models.Model):
    #CHAVES ESTRANGEIRAS#
    alunos_ra = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)

    np1 = models.IntegerField(blank=True, null=True)
    np2 = models.IntegerField(blank=True, null=True)
    np3 = models.IntegerField(blank=True, null=True)
    npa = models.IntegerField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
