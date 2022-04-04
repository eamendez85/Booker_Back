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
def estudiante_detalle_api_view(request, doc):
    #consulta
    estudiante = Estudiantes.objects.filter(doc_estudiante=doc).first()
    
    #validacion
    if estudiante:
    
        #get
        if request.method=='GET':
            estudiante_serializer= EstudiantesListSerializer(estudiante)
            return Response(estudiante_serializer.data, status = status.HTTP_200_OK)

        #Actualizar
        elif request.method =='PUT':
            estudiante_serializer = UsuariosSerializer(usuario, data = request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status = status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            estudiante.delete()
            return Response({"mensaje": "Estudiante eliminado correctamente"}, status = status.HTTP_200_OK)
    

    """
    elif request.method == 'POST':
        usuario_serializer = UsuariosSerializer(data = request.data)
        
        #validacion
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response({"mensaje": "Usuario creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    """
    #Crear
    