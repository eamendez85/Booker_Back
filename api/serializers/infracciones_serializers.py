from rest_framework import serializers
from api.models import Administradores, Ejemplares, Estudiantes, Infracciones, Libros, TipoInfraccion
from api.serializers.usuarios_serializers import AdministradoresInformacionGeneralSerializer, EstudianteInformacionGeneralSerializer

#Serializer de tipo infraccion para imprimirse en infracciones
class TipoInfraccionInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoInfraccion
        fields = ['nombre']

#Serializer de libros para imprimirse en infracciones
class LibrosInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields=['nombre','imagen_libro']


#Serializer de ejemplares para imprimirse en infracciones
class EjemplaresInfraccionesSerializer(serializers.ModelSerializer):
    id_libro = LibrosInfraccionesSerializer(many=False, read_only=True)

    class Meta:
        model = Ejemplares
        fields = ['id_ejemplar','id_libro','estado']


#Serializer infracciones para get
class InfraccionesListSerializer(serializers.ModelSerializer):
    id_administrador = AdministradoresInformacionGeneralSerializer(many=False, read_only=True)
    id_estudiante = EstudianteInformacionGeneralSerializer(many=False, read_only=True)
    ejemplares = EjemplaresInfraccionesSerializer(many = True, read_only=True )
    id_tipo_infraccion = TipoInfraccionInfraccionesSerializer(many= False, read_only = True)

    class Meta:
        model = Infracciones
        fields = ['id_infraccion','id_administrador','id_estudiante','ejemplares','id_tipo_infraccion','descripcion','estado' ]  

#Serializer infracciones para post
class InfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracciones
        fields = '__all__'

