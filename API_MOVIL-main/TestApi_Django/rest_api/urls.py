from django.urls import path
from rest_api.views import detalle_conductor, lista_alumnos, detalle_alumno, lista_conductor

urlpatterns=[
    path('alumnos', lista_alumnos, name="Lista de Alumnos"),
    path('alumno/<int:idAlumno>', detalle_alumno, name="Detalle Alumno"),
    path('conductores', lista_conductor, name="Lista de Conductores"),
    path('conductores/<int:idConductor>', detalle_conductor, name="Detalle Conductor"),

]