from django.forms import ValidationError
from rest_framework import serializers
from api.models import Autores, Editoriales, Grados, Grupos, Categorias

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