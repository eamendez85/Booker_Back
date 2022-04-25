from dataclasses import fields
from django.forms import ValidationError
from rest_framework import serializers
from api.models import Autores, DePrestamos, Editoriales, Ejemplares, Estudiantes, Favoritos, Grados, Grupos, Categorias, Idiomas, Infracciones, Libros, Prestados, TipoInfraccion

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

    categorias = CategoriasSerializer(many=True, read_only=True)
    autores = AutoresSerializer(many=True, read_only=True)
    id_editorial = serializers.StringRelatedField()
    id_idioma = serializers.StringRelatedField()

    class Meta:
        model = Libros
        fields = ['id_libro', 'isbn', 'imagen_libro', 'nombre', 'id_editorial', 'edicion','autores','id_idioma','categorias','descripcion', 'numero_paginas','alto','ancho','peso','presentacion','anexos','palabras_clave','estado']



class LibrosInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields=['nombre','imagen_libro']

class EstudianteInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['doc_estudiante','nombres','apellidos']


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

class EjemplaresInfraccionesSerializer(serializers.ModelSerializer):
    id_libro = LibrosInfraccionesSerializer(many=False, read_only=True)

    class Meta:
        model = Ejemplares
        fields = ['id_ejemplar','id_libro','estado']

#Serializer Tipo infracciones
class TipoInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInfraccion
        fields = '__all__'   

class TipoInfraccionInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoInfraccion
        fields = ['nombre']

#Serializer infracciones
class InfraccionesListSerializer(serializers.ModelSerializer):

    id_estudiante = EstudianteInfraccionesSerializer(many=False, read_only=True)
    ejemplares = EjemplaresInfraccionesSerializer(many = True, read_only=True )
    id_tipo_infraccion = TipoInfraccionInfraccionesSerializer(many= False, read_only = True)

    class Meta:
        model = Infracciones
        fields = ['id_infraccion','id_estudiante','ejemplares','id_tipo_infraccion','descripcion']  

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