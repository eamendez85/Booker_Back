from telnetlib import STATUS
from requests import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Categorias, Grados, Grupos
from api.serializers.general_serializers import CategoriasSerializer, GradosSerializer, GruposSerializer


#Viewset del modelo grados
class GradoViewSet(viewsets.ModelViewSet):
    serializer_class = GradosSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return GradosSerializer.Meta.model.objects.all()
        return Grados.objects.filter(id_grado = pk).first()

    def create(self, request):
        serializer = GradosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Se ha creado el grado correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        grado = Grados.objects.filter(id_grado = pk).first()
        serializer = GradosSerializer(grado, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        grado = Grados.objects.filter(id_grado = pk).first()
        grado.delete()
        return Response({'message':'Grado eliminado correctamente'}, status= status.HTTP_200_OK)
        
#ViewSet del modelo grupos
class GruposViewSet(viewsets.ModelViewSet):
    serializer_class = GruposSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return GruposSerializer.Meta.model.objects.all()
        return Grupos.objects.filter(id_grado = pk).first()

#ViewSet del modelo categorias
class CategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriasSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return CategoriasSerializer.Meta.model.objects.all()
        return Categorias.objects.filter(id_grado = pk).first()