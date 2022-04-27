from rest_framework import serializers
from api.models import DePrestamos
from api.serializers.ejemplares_serializers import EjemplaresListSerializer
from api.serializers.usuarios_serializers import AdministradoresInformacionGeneralSerializer, EstudianteInformacionGeneralSerializer

#Serializer DePrestamos
class DetallePrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DePrestamos
        fields = '__all__'

class DetallePrestamosListSerializer(serializers.ModelSerializer):

    id_administrador = AdministradoresInformacionGeneralSerializer(many=False, read_only=True)
    id_estudiante = EstudianteInformacionGeneralSerializer(many=False, read_only=True)
    ejemplares = EjemplaresListSerializer(many = True, read_only=True )

    class Meta:
        model = DePrestamos
        fields = ['id_de_prestamo','id_estudiante','id_administrador','ejemplares','fec_prestamo','fec_devolucion','estado']    