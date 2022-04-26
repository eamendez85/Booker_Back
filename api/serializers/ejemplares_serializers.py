from dataclasses import fields
from api.models import Ejemplares, Libros
from rest_framework import serializers

class LibrosEjemplaresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Libros
        fields = ['isbn', 'imagen_libro','nombre','autores','categorias','descripcion']

#Serializer Ejemplares
class EjemplaresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ejemplares
        fields = '__all__'   

class EjemplaresListSerializer(serializers.ModelSerializer):

    id_libro = LibrosEjemplaresSerializer(many=False, read_only=True)

    class Meta:
        model = Ejemplares
        fields = ['id_ejemplar','num_ejemplar','estado','id_libro']


