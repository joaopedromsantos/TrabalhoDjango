from rest_framework import viewsets
from Estagio import models
from Estagio.api import serializers

class EstagioViewSet(viewsets.ModelViewSet):
    queryset = models.Estagio.objects.all()
    serializer_class = serializers.EstagioSerializer

