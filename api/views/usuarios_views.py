from functools import partial
from pydoc import doc
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Usuario
from api.serializers.usuarios_serializers import *
from rest_framework import status
from rest_framework import viewsets

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuariosListSerializer
    
    def get_queryset(self, pk=None):
        if pk == None:
            return UsuariosListSerializer.Meta.model.objects.all()
        return Usuario.objects.filter(doc = pk).first()

    def create(self, request):
        serializer = UsuariosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Se ha agregado el usuario correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        usuario = Usuario.objects.filter(doc = pk).first()
        serializer = UsuariosSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Usuario actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        usuario = Usuario.objects.filter(doc = pk).first()
        serializer = UsuariosSerializer(usuario, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Usuario actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        usuario = Usuario.objects.filter(doc = pk).first()
        usuario.delete()
        return Response({'message':'Usuario eliminado correctamente'}, status= status.HTTP_200_OK)

class EstudiantesViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiantesListSerializer
    
    def get_queryset(self, pk=None):
        print("ENTRASSSSSSSSSS")
        if pk == None:
            print("TODOS")
            return EstudiantesSerializer.Meta.model.objects.all()
        return Estudiantes.objects.filter(doc = pk).first()

    def create(self, request):
        usuario_serializer = UsuariosSerializer(data = request.data['doc_estudiante'])
        data_estudiante = request.data
        data_usuario = request.data['doc_estudiante']
        data_usuario['tipo_usuario'] = 'E'
        data_estudiante['doc_estudiante']=data_usuario['doc']
        estudiante_serializer = EstudiantesSerializer(data = data_estudiante)
        

        #validacion usuario
        if usuario_serializer.is_valid():
            usuario_serializer.save()

        #validacion estuidante
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response({"mensaje": "Estudiante creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(estudiante_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        usuario = Usuario.objects.filter(doc = pk).first()
        estudiante = Estudiantes.objects.filter(doc_estudiante = pk).first()
        
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
        data_usuario['tipo_usuario'] = 'E'
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
def bibliotecarios_api_view(request):
    
    #listado
    if request.method == 'GET':
        #consulta

        bibliotecarios= Bibliotecarios.objects.all()
        bibliotecarios_serializer = BibliotecariosListSerializer(bibliotecarios, many=True)
        return Response(bibliotecarios_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        data_bibliotecario = request.data
        data_usuario = request.data['doc_bibliotecario']
        data_usuario['tipo_usuario'] = 'B'
        data_bibliotecario['doc_bibliotecario']=data_usuario['doc']
        
        usuario_serializer = UsuariosSerializer(data = data_usuario)
        bibliotecario_serializer = BibliotecariosSerializer(data = data_bibliotecario)
        

        #validacion
        print("USUARIOO", usuario_serializer)
        if usuario_serializer.is_valid():
            usuario_serializer.save()

        #validacion
        if bibliotecario_serializer.is_valid():
            bibliotecario_serializer.save()
            return Response({"mensaje": "bibliotecario creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(bibliotecario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bibliotecario_detalle_api_view(request, pk):
    #consulta
    bibliotecario = Bibliotecarios.objects.filter(doc_bibliotecario=pk).first()
    usuario = Usuario.objects.filter(doc=pk).first()
    
    #validacion
    if bibliotecario:
    
        #get
        if request.method=='GET':
            bibliotecario_serializer= BibliotecariosListSerializer(bibliotecario)
            return Response(bibliotecario_serializer.data, status = status.HTTP_200_OK)


        #Actualizar
        elif request.method =='PUT':
            data_bibliotecario = request.data
            data_usuario = request.data['doc_bibliotecario']
            data_bibliotecario['doc_bibliotecario'] = data_usuario['doc']
            usuario_serializer = UsuariosSerializer(usuario, data = data_usuario, partial=True)
            bibliotecario_serializer = BibliotecariosSerializer(bibliotecario, data = data_bibliotecario)
            
            if usuario_serializer.is_valid():
                usuario_serializer.save()
            
            if bibliotecario_serializer.is_valid():
                bibliotecario_serializer.save()
                return Response({"mensaje": "bibliotecario actualizado correctamente"}, status = status.HTTP_200_OK)
            return Response(bibliotecario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

        elif request.method == 'DELETE':
            usuario.delete()
            bibliotecario.delete()
            return Response({"mensaje": "bibliotecario eliminado correctamente"}, status = status.HTTP_200_OK)
    

    
    return Response({'mensaje': "Este bibliotecario no existe"}, status = status.HTTP_400_BAD_REQUEST)
    