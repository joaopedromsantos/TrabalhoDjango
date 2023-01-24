from rest_framework import serializers
from Disciplina import models

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = '__all__'


class DisciplinaSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome', 'carga_horaria']

class DisciplinaSerializerOut2(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome', 'carga_horaria']

class DisciplinaSerializerOut3(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome']