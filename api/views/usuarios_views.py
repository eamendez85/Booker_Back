from functools import partial
from pydoc import doc
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Usuario
from api.serializers.usuarios_serializers import *
from rest_framework import status, filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['doc_estudiante__usuario_activo', 'id_grado']
    search_fields = ['doc_estudiante__doc', 'nombres','apellidos']

    
    
    def get_queryset(self, pk=None):
        if pk == None:
            return EstudiantesSerializer.Meta.model.objects.all()
        return Estudiantes.objects.filter(id_estudiante = pk).first()

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

        #validacion estudiante
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response({"mensaje": "Estudiante creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(estudiante_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        estudiante = Estudiantes.objects.filter(id_estudiante = pk).first()
        
        data_estudiante = request.data
        data_usuario = request.data['doc_estudiante']
        doc_usuario = data_usuario['doc']
        usuario = Usuario.objects.filter(doc = doc_usuario).first()

        data_estudiante['doc_estudiante'] = doc_usuario
        usuario_serializer = UsuariosSerializer(usuario, data = data_usuario, partial=True)
        estudiante_serializer = EstudiantesSerializer(estudiante, data = data_estudiante)
        
        if usuario_serializer.is_valid():
            usuario_serializer.save()
        
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response({"mensaje": "Estudiante actualizado correctamente"}, status = status.HTTP_200_OK)
        return Response(estudiante_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        estudiante = Estudiantes.objects.filter(id_estudiante = pk).first()
        doc_estudiante = estudiante.doc_estudiante.doc
        usuario = Usuario.objects.filter(doc = doc_estudiante).first()
        
        usuario.delete()
        estudiante.delete()
        return Response({'message':'Estudiante eliminado correctamente'}, status= status.HTTP_200_OK)


class BibliotecariosViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['doc_bibliotecario__usuario_activo']
    search_fields = ['doc_bibliotecario__doc', 'nombres','apellidos']

    serializer_class = BibliotecariosListSerializer
    
    def get_queryset(self, pk=None):
        if pk == None:
            return BibliotecariosSerializer.Meta.model.objects.all()
        return Bibliotecarios.objects.filter(id_estudiante = pk).first()

    def create(self, request):
        usuario_serializer = UsuariosSerializer(data = request.data['doc_bibliotecario'])
        data_bibliotecario = request.data
        data_usuario = request.data['doc_bibliotecario']
        data_usuario['tipo_usuario'] = 'B'
        data_bibliotecario['doc_bibliotecario']=data_usuario['doc']
        bibliotecario_serializer = BibliotecariosSerializer(data = data_bibliotecario)
        

        #validacion usuario
        if usuario_serializer.is_valid():
            usuario_serializer.save()

        #validacion bibliotecario
        if bibliotecario_serializer.is_valid():
            bibliotecario_serializer.save()
            return Response({"mensaje": "Bibliotecario creado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(bibliotecario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        bibliotecario = Bibliotecarios.objects.filter(id_bibliotecario = pk).first()
        
        data_bibliotecario = request.data
        data_usuario = request.data['doc_bibliotecario']
        doc_usuario = data_usuario['doc']
        usuario = Usuario.objects.filter(doc = doc_usuario).first()

        data_bibliotecario['doc_bibliotecario'] = doc_usuario
        usuario_serializer = UsuariosSerializer(usuario, data = data_usuario, partial=True)
        bibliotecario_serializer = BibliotecariosSerializer(bibliotecario, data = data_bibliotecario)
        
        if usuario_serializer.is_valid():
            usuario_serializer.save()
        
        if bibliotecario_serializer.is_valid():
            bibliotecario_serializer.save()
            return Response({"mensaje": "Bibliotecario actualizado correctamente"}, status = status.HTTP_200_OK)
        return Response(bibliotecario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        bibliotecario = Bibliotecarios.objects.filter(id_bibliotecario = pk).first()
        doc_bibliotecario = bibliotecario.doc_bibliotecario.doc
        usuario = Usuario.objects.filter(doc = doc_bibliotecario).first()
        
        usuario.delete()
        bibliotecario.delete()
        return Response({'message':'Bibliotecario eliminado correctamente'}, status= status.HTTP_200_OK)