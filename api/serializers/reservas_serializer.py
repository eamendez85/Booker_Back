from rest_framework import serializers
from api.models import Reservas
from api.serializers.ejemplares_serializers import EjemplaresListSerializer
from api.serializers.usuarios_serializers import EstudianteInformacionGeneralSerializer

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'

class ReservasListSerializer(serializers.ModelSerializer):
    id_estudiante = EstudianteInformacionGeneralSerializer(many = False, read_only=True)
    ejemplares = EjemplaresListSerializer(many = True, read_only = True)

    class Meta:
        model = Reservas
        fields = ['id_reserva','id_estudiante','ejemplares','estado']