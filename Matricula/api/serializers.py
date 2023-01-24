from rest_framework import serializers

from Aluno.api.serializers import AlunoSerializerOut2
from Disciplina.api.serializers import DisciplinaSerializerOut3
from Matricula import models

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = '__all__'

class MatriculaSerializerOut(serializers.ModelSerializer):
    alunos_ra = AlunoSerializerOut2()
    disciplina_id = DisciplinaSerializerOut3()

    class Meta:
        model = models.Matricula
        fields = ['alunos_ra', 'npa', 'disciplina_id']
