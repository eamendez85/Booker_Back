from rest_framework.response import Response
from api.serializers.libros_serializers import LibrosListSerializer, LibrosSerializer
from rest_framework import viewsets
from api.models import Ejemplares, Libros
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend

class LibrosViewSet(viewsets.ModelViewSet):
    
    serializer_class = LibrosListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


    #Para poder filtrar, se ingresa en la url ?(nombre del campo)=(valor que se quiere filtrar)
    #por ejemplo: ?nombre=el principito
    filterset_fields= ['estado','autores__id_autor','categorias__id_categoria', 'id_idioma','id_editorial']


    #Para poder buscar, se ingresa en la url ?search=(valor que se quiere buscar)
    #por ejemplo: ?search=novela, aqui se puede poner cualquier caracter, letra o palabra para poder buscarse
    search_fields = ['isbn','nombre','categorias__nombre','autores__nombres','autores__apellidos']

    #Para poder ordenar la información de manera ascendente es ?ordering=(campo que quiere ordenar en especifico) el campo tiene que estar 
    #igual de escrito que los campos de ordering_fields
    # ejemplo ?ordering=id_idioma__nombre
    ordering_fields = ['isbn','nombre',
    'estado','categorias__nombre'
    ,'autores__nombres','autores__apellidos', 'id_libro'] 


    def get_queryset(self, pk=None):
        if pk == None:
            return LibrosListSerializer.Meta.model.objects.all()
        return LibrosListSerializer.objects.filter(id_libro = pk).first()
    
    def create (self, request):
        cant_ejemplares = request.data.get("cant_ejemplares")
        request.data.pop("cant_ejemplares")
        data_libro = request.data
        
        serializer_libro = LibrosSerializer(data = data_libro)
        
        if serializer_libro.is_valid():
            libro_guardado = serializer_libro.save()
            
            for item in range(cant_ejemplares):
                ejemplar = Ejemplares(num_ejemplar=(item+1), estado="D", id_libro=libro_guardado)
                ejemplar.save()
            return Response({'data':serializer_libro.data, 'message':'Se ha creado el libro y los ejemplares correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer_libro.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        #Cuando se cambie el estado a inactivo de un libro tambien cambie el estado de los ejemplares existentes
        libro = Libros.objects.filter(id_libro = pk).first()
        serializer_libro = LibrosSerializer(libro, data = request.data)
        estado_libro = request.data.get("estado")
        ejemplares_libro = Ejemplares.objects.filter(id_libro = pk)
        if serializer_libro.is_valid():
            if estado_libro == "IV":
                for ejemplar in ejemplares_libro: 
                    ejemplar.estado = "IV"
                    ejemplar.save()
                serializer_libro.save()
                return Response({'data' : serializer_libro.data, 'message':'Libro actualizado correctamente'}, status= status.HTTP_200_OK)
            else: 
                serializer_libro.save()
                return Response({'data' : serializer_libro.data, 'message':'Libro actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer_libro.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        libro = Libros.objects.filter(id_libro = pk).first()
        ejemplares = Ejemplares.objects.filter(id_libro = pk)
        for ejemplar in ejemplares:
            ejemplar.delete()
        libro.delete()
        return Response({'message':'Libro y ejemplares eliminados correctamente'}, status= status.HTTP_200_OK)