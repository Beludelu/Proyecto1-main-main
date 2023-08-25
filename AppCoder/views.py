from django.shortcuts import render
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from AppCoder.models import Curso
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import Curso_form

def inicio(request):
        return render( request , "padre.html")

def ver_cursos(request):
        curso = Curso.objects.all() #comunicacion con la base de datos directo
        dicc = {"curso":curso}
        padre = loader.get_template("padre.html")
        documento = padre.render(dicc)
        return HttpResponse(documento) #aca me va a venir la plantilla renderizada con los datos


def profesores(request):
        return render( request , "profesores.html") #lo unico que esta haciendo aca es renderizarlo

def alumnos(request):
        return render( request , "alumnos.html")

def curso_formulario(request):
        if request.method == "POST":

            mi_formulario = Curso_form( request.POST )
            if mi_formulario.is_valid():
                datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , comision=datos["comision"])
            curso.save()
            return render( request , "formulario.html")      
        return render( request , "formulario.html")

def curso(request):
       return render( request , "curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"Cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
