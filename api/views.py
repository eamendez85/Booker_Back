from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Usuario
from api.serializers import *
from rest_framework import status


@api_view(['GET', 'POST'])
def usuario_api_view(request):
    
    #listado
    if request.method == 'GET':
        #consulta
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuariosListSerializer(usuarios, many=True)
        return Response(usuarios_serializer.data, status = status.HTTP_200_OK)
    
    #Crear
    elif request.method == 'POST':
        usuario_serializer = UsuariosSerializer(data = request.data)
        
        #validacion
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response({"mensaje": "Usuario creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detalle_api_view(request, pk):
    #consulta
    usuario = Usuario.objects.filter(doc=pk).first()
    
    #validacion
    if usuario:
    
        #get
        if request.method=='GET':
            usuario_serializer= UsuariosListSerializer(usuario)
            return Response(usuario_serializer.data, status = status.HTTP_200_OK)
        
        #Actualizar
        elif request.method =='PUT':
            usuario_serializer = UsuariosSerializer(usuario, data = request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status = status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #eliminar
        elif request.method == 'DELETE':
            usuario.delete()
            return Response({"mensaje": "Usuario eliminado correctamente"}, status = status.HTTP_200_OK)
        
    return Response({'mensaje': "Este usuario no existe"}, status = status.HTTP_400_BAD_REQUEST)