from rest_framework import serializers
from api.models import Infracciones, Libros, TipoInfraccion
from api.serializers.ejemplares_serializers import EjemplaresListSerializer
from api.serializers.general_serializers import TipoInfraccionesSerializer
from api.serializers.usuarios_serializers import BibliotecariosInformacionGeneralSerializer, EstudianteInformacionGeneralSerializer


#Serializer de libros para imprimirse en infracciones
class LibrosInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields=['nombre','imagen_libro']



#Serializer infracciones para get
class InfraccionesListSerializer(serializers.ModelSerializer):
    id_bibliotecario = BibliotecariosInformacionGeneralSerializer(many=False, read_only=True)
    id_estudiante = EstudianteInformacionGeneralSerializer(many=False, read_only=True)
    ejemplares = EjemplaresListSerializer(many = True, read_only=True )
    id_tipo_infraccion = TipoInfraccionesSerializer(many= False, read_only = True)

    class Meta:
        model = Infracciones
        fields = ['id_infraccion','id_bibliotecario', 'id_estudiante','ejemplares','id_tipo_infraccion','descripcion','estado' ]  

#Serializer infracciones para post
class InfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracciones
        fields = '__all__'

