from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers.libros_serializers import LibrosListSerializer, LibrosSerializer
from rest_framework import viewsets
from api.models import Libros
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend

class LibrosViewSet(viewsets.ModelViewSet):
    serializer_class = LibrosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


    #Para poder filtrar, se ingresa en la url ?(nombre del campo)=(valor que se quiere filtrar)
    #por ejemplo: ?nombre=el principito
    filterset_fields= ['isbn','nombre','estado','autores','categorias','id_idioma__nombre','id_editorial__nombre']


    #Para poder buscar, se ingresa en la url ?search=(valor que se quiere buscar)
    #por ejemplo: ?search=novela, aqui se puede poner cualquier caracter, letra o palabra para poder buscarse
    search_fields = ['isbn','nombre',
    'palabras_clave','id_editorial__nombre','id_idioma__nombre','categorias__nombre'
    ,'autores__nombres','autores__apellidos']

    #Para poder ordenar la información de manera ascendente es ?ordering=(campo que quiere ordenar en especifico) el campo tiene que estar 
    #igual de escrito que los campos de ordering_fields
    # ejemplo ?ordering=id_idioma__nombre
    ordering_fields = ['isbn','nombre',
    'estado','categorias__nombre'
    ,'autores__nombres','autores__apellidos']



    def get_queryset(self, pk=None):
        if pk == None:
            return LibrosListSerializer.Meta.model.objects.all()
        return LibrosListSerializer.objects.filter(id_libro=pk).first()

    def create (self, request):
        serializer_libro = LibrosSerializer(data = request.data)
        if serializer_libro.is_valid():
            serializer_libro.save()
            return Response({'data':serializer_libro.data, 'message':'Se ha creado el libro correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer_libro.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        libro = Libros.objects.filter(id_libro = pk).first()
        serializer_libro = LibrosSerializer(libro, data = request.data)
        if serializer_libro.is_valid():
            serializer_libro.save()
            return Response({'data' : serializer_libro.data, 'message':'Libro actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer_libro.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        libro = Libros.objects.filter(id_libro = pk).first()
        libro.delete()
        return Response({'message':'Libro eliminado correctamente'}, status= status.HTTP_200_OK)