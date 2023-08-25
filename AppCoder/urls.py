from django.urls import path
from . import views

urlpatterns = [
    path("" , views.inicio , name="inicio"),
    path("ver_cursos" , views.ver_cursos),
#    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("alta_cursos", views.curso_formulario),
    path("curso" , views.curso),
    path("buscar" , views.buscar),
]


