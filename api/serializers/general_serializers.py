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


    def to_representation(self, instance):
        return{
            'id libro': instance.id_libro,
            'isbn': instance.isbn,
            'Nombre del libro': instance.nombre,
            'Editorial del libro': instance.id_editorial.nombre,
            'Edición del libro': instance.edicion,
            'Idioma': instance.id_idioma.nombre,
            'Descripción':instance.descripcion,
            'Numero de paginas':instance.numero_paginas,
            'Alto del libro':instance.alto,
            'Ancho del libro':instance.ancho,
            'Peso del libro':instance.peso,
            'Presentación':instance.presentacion,
            'Anexos del libro':instance.anexos,
            'Palabras clave':instance.palabras_clave,
            'Estado':instance.estado,
        }

#Serializer favoritos
class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Estudiante':instance.id_estudiante.nombres,

        }

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