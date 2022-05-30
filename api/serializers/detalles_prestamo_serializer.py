from rest_framework import serializers
from api.models import DePrestamos, Prestamos
from api.serializers.ejemplares_serializers import EjemplaresListSerializer
from api.serializers.usuarios_serializers import BibliotecariosInformacionGeneralSerializer, EstudianteInformacionGeneralSerializer

#Serializers Prestamos
class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'
        
class PrestamosListSerializer(serializers.ModelSerializer):
    
    id_ejemplar = EjemplaresListSerializer(read_only=True)
    
    class Meta:
        model = Prestamos
        fields = ['id_prestamo', 'fec_devolucion', 'estado', 'id_ejemplar']

#Serializer DePrestamos
class DetallePrestamosSerializer(serializers.ModelSerializer):
    
    prestamos = PrestamosSerializer(many=True, required=False)
    
    class Meta:
        model = DePrestamos
        fields = ['id_de_prestamo','id_estudiante', 'prestamos','id_bibliotecario','fec_prestamo','estado']

class DetallePrestamosListSerializer(serializers.ModelSerializer):

    id_bibliotecario = BibliotecariosInformacionGeneralSerializer(many=False, read_only=True)
    id_estudiante = EstudianteInformacionGeneralSerializer(many=False, read_only=True)
    prestamos = PrestamosListSerializer(many=True, read_only=True)

    class Meta:
        model = DePrestamos
        fields = ['id_de_prestamo','id_estudiante', 'prestamos','id_bibliotecario','fec_prestamo','estado']    