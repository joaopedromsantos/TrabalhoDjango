from rest_framework import serializers
from Professor import models
from Disciplina.api.serializers import DisciplinaSerializer, DisciplinaSerializerOut


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = '__all__'


class ProfessorSerializerOut(serializers.ModelSerializer):
    disciplina_id = DisciplinaSerializerOut()

    class Meta:
        model = models.Professor
        fields = ['disciplina_id']
