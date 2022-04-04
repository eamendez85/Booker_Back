from dataclasses import field, fields
from rest_framework import serializers
from api.models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields="__all__"
        
    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
    
    def update(self, instance, validated_data):
        update_usuario = super().update(instance, validated_data)
        update_usuario.set_password(validated_data['password'])
        update_usuario.save()
        return update_usuario
    
    
    
    """ Validacion
    def validate_name(self, value):
        if 'pepe' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con este nombre') 
        return value
    """

class EstudiantesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields  ="__all__"
            
class UsuariosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields="__all__"
    """"
    def to_representation(self, instance):
        return {
            'id_libro': instance.id_libro,
            'isbn': instance.isbn,
            'nombre':instance.nombre,
            'edicion':instance.edicion,
            'descripcion':instance.descripcion,
            'numero de paginas':instance.numero_paginas,
            'numero de capitulos':instance.numero_capitulos,
            'alto':instance.alto,
            'ancho':instance.ancho,
            'peso':instance.peso,
            'presentacion':instance.presentacion,
            'anexos':instance.anexos,
            'palabras clave':instance.palabras_clave,
            'estado':instance.estado,
        }
        
    """