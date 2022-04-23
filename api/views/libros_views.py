from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers.general_serializers import LibrosSerializer
from api.serializers.usuarios_serializers import *
from rest_framework import status

@api_view(['GET', 'POST'])
def libros_view(request):
    if request.method == 'GET':
        libros = Libros.objects.all()
        librosSerializer = LibrosSerializer(libros, many=True)
        return Response(librosSerializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        librosSerializer = LibrosSerializer(data = request.data)
        #validacion
        if librosSerializer.is_valid():
            librosSerializer.save()
            return Response({"mensaje": "Libro agregado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(librosSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def libro_detalle_view(request, pk):
    #consulta
    libro = Libros.objects.filter(id_libro=pk).first()
    
    #validacion
    if libro:
    
        #get
        if request.method=='GET':
            libroSerializer= LibrosSerializer(libro)
            return Response(libroSerializer.data, status = status.HTTP_200_OK)
        
        #Actualizar
        elif request.method =='PUT':
                
            libroSerializer = LibrosSerializer(libro, data = request.data)
            if libroSerializer.is_valid():
                libroSerializer.save()
                return Response(libroSerializer.data, status = status.HTTP_200_OK)
            return Response(libroSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method =='PATCH':
                
            libroSerializer = LibrosSerializer(libro, data = request.data, partial=True)
            if libroSerializer.is_valid():
                libroSerializer.save()
                return Response(libroSerializer.data, status = status.HTTP_200_OK)
            return Response(libroSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #eliminar
        elif request.method == 'DELETE':
            libro.delete()
            return Response({"mensaje": "Libro eliminado correctamente"}, status = status.HTTP_200_OK)
        
    return Response({'mensaje': "Este libro no existe"}, status = status.HTTP_400_BAD_REQUEST)

