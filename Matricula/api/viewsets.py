from rest_framework import viewsets, filters
from Matricula import models
from Matricula.api import serializers
from Matricula.api.serializers import MatriculaSerializer, MatriculaSerializerOut
from Matricula.models import Matricula


class MatriculaViewSet(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializer
    queryset = models.Matricula.objects.all()




class MatriculaViewSetSearch(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializerOut
    def get_queryset(self):
        alunos_ra = self.request.query_params.get('alunos_ra', None)

        if alunos_ra:
            queryset = models.Matricula.objects.filter(alunos_ra=alunos_ra)
            return queryset

        else:
            return models.Matricula.objects.all()


