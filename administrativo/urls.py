from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.index, name='index'),  # Ruta de ejemplo
    path('listado_estudiantes', views.listado_estudiantes, name = 'estudiantes')
]