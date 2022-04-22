from dataclasses import fields
from django.forms import ValidationError
from rest_framework import serializers
from api.models import Autores, DePrestamos, Editoriales, Ejemplares, Favoritos, Grados, Grupos, Categorias, Idiomas, Infracciones, Libros, Prestados, TipoInfraccion

#Serializer grados
class GradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grados
        fields = '__all__'

#Serializer grupos
class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = '__all__'

#Serializer categorias
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

#Serializer autores
class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'
        
#Serializer editoriales
class EditorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editoriales
        fields = '__all__'

#Serializer idiomas
class IdiomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idiomas
        fields = '__all__'

#Serializer libros
class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'

    editorial = serializers.StringRelatedField()
    idioma = serializers.StringRelatedField()

    def to_representation(self, instance):
        return{
            'id libro': instance.id_libro,
            'isbn': instance.isbn,
            'Imagen de libro': instance.imagen_libro,
            'Nombre del libro': instance.nombre,
            'Editorial del libro': instance.editorial.nombre,
            'Edición del libro': instance.edicion,
            'Autores': instance.autores,
            'Idioma': instance.idioma.nombre,
            'categorias': instance.categorias,
            

        }

#Serializer favoritos
class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'

#Serializer Ejemplares
class EjemplaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejemplares
        fields = '__all__'   

#Serializer Tipo infracciones
class TipoInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInfraccion
        fields = '__all__'   

#Serializer infracciones
class InfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infracciones
        fields = '__all__'   

#Serializer DePrestamos
class DetallePrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DePrestamos
        fields = '__all__'

#Serializer prestados
class PrestadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestados
        fields = '__all__'