from rest_framework import viewsets
from Disciplina import models
from Disciplina.api import serializers

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializer