from rest_framework import serializers
from Aluno import models
from Estagio.api.serializers import EstagioSerializer

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'

class AlunoSerializerOut(serializers.ModelSerializer):
    Estagio_id = EstagioSerializer()

    class Meta:
        model = models.Aluno
        fields = '__all__'


class AlunoSerializerOut2(serializers.ModelSerializer):

    class Meta:
        model = models.Aluno
        fields = ['nome']


