from dataclasses import fields
from rest_framework import serializers
from api.models import Autores, Editoriales, Ejemplares, Estudiantes, Favoritos, Grados, Grupos, Categorias, Idiomas, Infracciones, Libros, TipoInfraccion

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

#Serializer Tipo infracciones
class TipoInfraccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInfraccion
        fields = '__all__'   



#Serializer prestado