from dataclasses import field, fields
from rest_framework import serializers
from api.models import Usuario, Estudiantes, Bibliotecarios
from api.serializers.general_serializers import GradosSerializer, GruposSerializer

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
        
        if "password" not in validated_data:
            
            update_usuario = super().update(instance, validated_data)
            update_usuario.save()
            return update_usuario
        else:
            update_usuario = super().update(instance, validated_data)
            update_usuario.set_password(validated_data['password'])
            update_usuario.save()
            return update_usuario

class UsuariosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('password',)

class EstudiantesListSerializer(serializers.ModelSerializer):

    doc_estudiante = UsuariosListSerializer(many=False,  read_only=True)
    id_grado = GradosSerializer(many=False)
    id_grupo = GruposSerializer(many=False)


    class Meta:
        model = Estudiantes
        fields  =['id_estudiante', 'tipodoc', 'nombres', 'apellidos', 'telefono',  'direccion', 'doc_estudiante', 'id_grado', 'id_grupo']



class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields="__all__"


class EstudianteInformacionGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['id_estudiante','doc_estudiante','nombres','apellidos']
        

class BibliotecariosListSerializer(serializers.ModelSerializer):
    
    doc_bibliotecario = UsuariosListSerializer(many=False,  read_only=True)


    class Meta:
        model = Bibliotecarios
        fields  =['id_bibliotecario', 'tipodoc', 'nombres', 'apellidos', 'telefono',  'direccion', 'doc_bibliotecario']



class BibliotecariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecarios
        fields="__all__"

class BibliotecariosInformacionGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecarios
        fields = ['id_bibliotecario','doc_bibliotecario','nombres','apellidos']