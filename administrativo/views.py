from django.shortcuts import render
from django.http import HttpResponse 
from administrativo.models import Estudiante

# Create your views here.
def index(request):
    return HttpResponse('Hola Mundo desde Python')

def listado_estudiantes(request):

    estudiantes = Estudiante.objects.all()
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render (request, 'listado_estudiantes.html', informacion_template)