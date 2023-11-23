from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Alumno, Conductor
from .serializers import AlumnoSerializer, ConductorSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_alumno(request, idAlumno):
    try:
        alumno = Alumno.objects.get(idAlumno=idAlumno)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AlumnoSerializer(alumno)
    return Response(serializer.data)

@api_view(['GET'])
def lista_conductor(request):
    conductores = Conductor.objects.all()
    serializer = ConductorSerializer(conductores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detalle_conductor(request, idConductor):
    try:
        conductor = Conductor.objects.get(idConductor=idConductor)
    except Conductor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ConductorSerializer(conductor)
    return Response(serializer.data)

