"""Escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from Aluno.api.viewsets import AlunoViewSet
from Disciplina.api.viewsets import DisciplinaViewSet
from Estagio.api.viewsets import EstagioViewSet
from Matricula.api.viewsets import MatriculaViewSet, MatriculaViewSetSearch
from Professor.api.viewsets import ProfessorViewSet
from Aluno.api.viewsets import AlunoViewSetOut
from Professor.api.viewsets import ProfessorViewSetOut

router = routers.DefaultRouter()

router.register(r'listaAlunos', AlunoViewSet, basename='ListaAlunos')
router.register(r'listaDisciplinas', DisciplinaViewSet, basename='listaDisciplinas')
router.register(r'listaEstagios', EstagioViewSet, basename='listaEstagios')
router.register(r'listaMatriculas', MatriculaViewSet, basename='listaMatriculas')
router.register(r'listaProfessores', ProfessorViewSet, basename='listaProfessores')
router.register(r'ViewAlunos', AlunoViewSetOut, basename='ViewAlunos')
router.register(r'ViewProfessores', ProfessorViewSetOut, basename='ViewProfessores')
router.register(r'SearchMatricula', MatriculaViewSetSearch, basename='SearchMatricula')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
