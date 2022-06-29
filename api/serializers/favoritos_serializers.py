from dataclasses import field
from rest_framework import serializers
from api.models import Estudiantes, Favoritos, Libros
from api.serializers.general_serializers import AutoresSerializer, CategoriasSerializer, EditorialesSerializer, IdiomasSerializer

#Serializer favoritos
class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'

class LibrosFavoritosSerializer(serializers.ModelSerializer):

    id_editorial = EditorialesSerializer(many=False, read_only=True)
    autores = AutoresSerializer(many=True, read_only=True)
    id_idioma = IdiomasSerializer(many=False, read_only=True)
    categorias = CategoriasSerializer(many=True, read_only=True)

    class Meta:
        model = Libros
        fields = ['id_libro','isbn','imagen_libro','nombre','autores','categorias','id_editorial','id_idioma']

class FavoritosListSerializer(serializers.ModelSerializer):
    
    libros = LibrosFavoritosSerializer(many = True, read_only=True)

    class Meta:
        model = Favoritos
        fields = ['id_favorito', 'id_estudiante','libros']

