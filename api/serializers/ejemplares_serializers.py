from dataclasses import fields
from api.models import Ejemplares, Libros
from rest_framework import serializers

from api.serializers.general_serializers import AutoresSerializer, CategoriasSerializer, EditorialesSerializer, IdiomasSerializer

class LibrosEjemplaresSerializer(serializers.ModelSerializer):
    
    autores = AutoresSerializer(many=True, read_only=True)
    id_idioma = IdiomasSerializer(many=False, read_only=True)
    categorias = CategoriasSerializer(many=True, read_only=True)

    class Meta:
        model = Libros
        fields = ['id_libro','isbn', 'imagen_libro','nombre','autores','categorias','descripcion','id_idioma']

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


