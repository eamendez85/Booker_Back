from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Usuario
from api.serializers.usuarios_serializers import *
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
    

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
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
        
        elif request.method =='PATCH':
                
            usuario_serializer = UsuariosSerializer(usuario, data = request.data, partial=True)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status = status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #eliminar
        elif request.method == 'DELETE':
            usuario.delete()
            return Response({"mensaje": "Usuario eliminado correctamente"}, status = status.HTTP_200_OK)
        
    return Response({'mensaje': "Este usuario no existe"}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def estudiantes_api_view(request):
    
    #listado
    if request.method == 'GET':
        #consulta

        estudiantes= Estudiantes.objects.all()
        estudiantes_serializer = EstudiantesListSerializer(estudiantes, many=True)
        return Response(estudiantes_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        usuario_serializer = UsuariosSerializer(data = request.data['doc_estudiante'])
        data_estudiante = request.data
        data_usuario = request.data['doc_estudiante']
        data_estudiante['doc_estudiante']=data_usuario['doc']
        estudiante_serializer = EstudiantesSerializer(data = data_estudiante)
        

        #validacion
        if usuario_serializer.is_valid():
            usuario_serializer.save()

        #validacion
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response({"mensaje": "Estudiante creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(estudiante_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detalle_api_view(request, pk):
    #consulta
    estudiante = Estudiantes.objects.filter(doc_estudiante=pk).first()
    usuario = Usuario.objects.filter(doc=pk).first()
    
    #validacion
    if estudiante:
    
        #get
        if request.method=='GET':
            estudiante_serializer= EstudiantesListSerializer(estudiante)
            return Response(estudiante_serializer.data, status = status.HTTP_200_OK)


        #Actualizar
        elif request.method =='PUT':
            data_estudiante = request.data
            data_usuario = request.data['doc_estudiante']
            data_estudiante['doc_estudiante'] = data_usuario['doc']
            usuario_serializer = UsuariosSerializer(usuario, data = data_usuario, partial=True)
            estudiante_serializer = EstudiantesSerializer(estudiante, data = data_estudiante)
            
            if usuario_serializer.is_valid():
                usuario_serializer.save()
            
            if estudiante_serializer.is_valid():
                estudiante_serializer.save()
                return Response({"mensaje": "Estudiante actualizado correctamente"}, status = status.HTTP_200_OK)
            return Response(estudiante_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

        elif request.method == 'DELETE':
            usuario.delete()
            estudiante.delete()
            return Response({"mensaje": "Estudiante eliminado correctamente"}, status = status.HTTP_200_OK)
    

    
    return Response({'mensaje': "Este estudiante no existe"}, status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST'])
def administradores_api_view(request):
    
    #listado
    if request.method == 'GET':
        #consulta

        administradores= Administradores.objects.all()
        administradores_serializer = AdministradoresListSerializer(administradores, many=True)
        return Response(administradores_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        usuario_serializer = UsuariosSerializer(data = request.data['doc_administrador'])
        data_administrador = request.data
        data_usuario = request.data['doc_administrador']
        data_administrador['doc_administrador']=data_usuario['doc']
        administrador_serializer = AdministradoresSerializer(data = data_administrador)
        

        #validacion
        if usuario_serializer.is_valid():
            usuario_serializer.save()

        #validacion
        if administrador_serializer.is_valid():
            administrador_serializer.save()
            return Response({"mensaje": "Administrador creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(administrador_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def administrador_detalle_api_view(request, pk):
    #consulta
    administrador = Administradores.objects.filter(doc_administrador=pk).first()
    usuario = Usuario.objects.filter(doc=pk).first()
    
    #validacion
    if administrador:
    
        #get
        if request.method=='GET':
            administrador_serializer= AdministradoresListSerializer(administrador)
            return Response(administrador_serializer.data, status = status.HTTP_200_OK)


        #Actualizar
        elif request.method =='PUT':
            data_administrador = request.data
            data_usuario = request.data['doc_administrador']
            data_administrador['doc_administrador'] = data_usuario['doc']
            usuario_serializer = UsuariosSerializer(usuario, data = data_usuario, partial=True)
            administrador_serializer = AdministradoresSerializer(administrador, data = data_administrador)
            
            if usuario_serializer.is_valid():
                usuario_serializer.save()
            
            if administrador_serializer.is_valid():
                administrador_serializer.save()
                return Response({"mensaje": "Administrador actualizado correctamente"}, status = status.HTTP_200_OK)
            return Response(administrador_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

        elif request.method == 'DELETE':
            usuario.delete()
            administrador.delete()
            return Response({"mensaje": "Administrador eliminado correctamente"}, status = status.HTTP_200_OK)
    

    
    return Response({'mensaje': "Este administrador no existe"}, status = status.HTTP_400_BAD_REQUEST)
    