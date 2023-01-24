from rest_framework import viewsets
from Aluno import models
from Aluno.api import serializers

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializer


class AlunoViewSetOut(viewsets.ModelViewSet):
    if models.Aluno.Estagio_id:
        queryset = models.Aluno.objects.all()
        serializer_class = serializers.AlunoSerializerOut

