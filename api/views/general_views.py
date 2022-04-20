from telnetlib import STATUS
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Autores, Categorias, Editoriales, Grados, Grupos
from api.serializers.general_serializers import AutoresSerializer, CategoriasSerializer, EditorialesSerializer, GradosSerializer, GruposSerializer


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
            return Response({'data' : serializer.data, 'message':'Se ha creado el grado correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        grado = Grados.objects.filter(id_grado = pk).first()
        serializer = GradosSerializer(grado, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message': "Grado actualizado correctamente"}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        grado = Grados.objects.filter(id_grado = pk).first()
        grado.delete()
        return Response({'message':'Grado eliminado correctamente'}, status= status.HTTP_200_OK)
        

#ViewSet del modelo grupos
class GruposViewSet(viewsets.ModelViewSet):
    serializer_class = GruposSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return GruposSerializer.Meta.model.objects.all()
        return Grupos.objects.filter(id_grupo = pk).first()

    def create(self, request):
        serializer = GruposSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Se ha creado el grupo correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        grupo = Grupos.objects.filter(id_grupo = pk).first()
        serializer = GruposSerializer(grupo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Grupo actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        grupo = Grupos.objects.filter(id_grupo = pk).first()
        grupo.delete()
        return Response({'message':'Grupo eliminado correctamente'}, status= status.HTTP_200_OK)
        

#ViewSet del modelo categorias
class CategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriasSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return CategoriasSerializer.Meta.model.objects.all()
        return Categorias.objects.filter(id_categoria = pk).first()

    def create(self, request):
            serializer = CategoriasSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado la categoria correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        categoria = Categorias.objects.filter(id_categoria = pk).first()
        serializer = CategoriasSerializer(categoria, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Categoria actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        categoria = Categorias.objects.filter(id_categoria = pk).first()
        categoria.delete()
        return Response({'message':'Categoria eliminada correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo autores
class AutoresViewset(viewsets.ModelViewSet):
    serializer_class = AutoresSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return AutoresSerializer.Meta.model.objects.all()
        return Autores.objects.filter(id_autor = pk).first()

    def create(self, request):
            serializer = AutoresSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado el autor correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        autor = Autores.objects.filter(id_autor = pk).first()
        serializer = AutoresSerializer(autor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Autor actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        autor = Autores.objects.filter(id_autor = pk).first()
        autor.delete()
        return Response({'message':'Autor eliminado correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo editoriales
class EditorialesViewSet(viewsets.ModelViewSet):
    serializer_class = EditorialesSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return EditorialesSerializer.Meta.model.objects.all()
        return Editoriales.objects.filter(id_editorial = pk).first()

    def create(self, request):
            serializer = EditorialesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado la editorial correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        editorial = Editoriales.objects.filter(id_editorial = pk).first()
        serializer = EditorialesSerializer(editorial, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Editorial actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        editorial = Editoriales.objects.filter(id_editorial = pk).first()
        editorial.delete()
        return Response({'message':'Editorial eliminada correctamente'}, status= status.HTTP_200_OK)