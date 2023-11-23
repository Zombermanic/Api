from rest_framework import serializers
from core.models import Alumno, Conductor

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['idAlumno', 'Gmail', 'password', 'user']

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ['idConductor', 'Gmail', 'password', 'user', 'autoMarca', 'autoPatente', 'valorViaje','HoraSalida']