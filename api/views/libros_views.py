from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers.general_serializers import LibrosSerializer
from api.models import Libros
from rest_framework import status

@api_view(['GET', 'POST'])
def libros_view(request):
    if request.method == 'GET':
        libros = Libros.objects.all()
        libros_serializer = LibrosSerializer(libros, many=True)
        return Response(libros_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        libros_serializer = LibrosSerializer(data = request.data)
        #validacion
        if libros_serializer.is_valid():
            libros_serializer.save()
            return Response({"mensaje": "Libro agregado correctamente"}, status = status.HTTP_201_CREATED)
        return Response(libros_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def libro_detalle_view(request, pk):
    #consulta
    libro = Libros.objects.filter(id_libro=pk).first()
    
    #validacion
    if libro:
    
        #get
        if request.method=='GET':
            libro_serializer= LibrosSerializer(libro)
            return Response(libro_serializer.data, status = status.HTTP_200_OK)
        
        #Actualizar
        elif request.method =='PUT':
                
            libro_serializer = LibrosSerializer(libro, data = request.data)
            if libro_serializer.is_valid():
                libro_serializer.save()
                return Response(libro_serializer.data, status = status.HTTP_200_OK)
            return Response(libro_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method =='PATCH':
                
            libro_serializer = LibrosSerializer(libro, data = request.data, partial=True)
            if libro_serializer.is_valid():
                libro_serializer.save()
                return Response(libro_serializer.data, status = status.HTTP_200_OK)
            return Response(libro_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #eliminar
        elif request.method == 'DELETE':
            libro.delete()
            return Response({"mensaje": "Libro eliminado correctamente"}, status = status.HTTP_200_OK)
        
    return Response({'mensaje': "Este libro no existe"}, status = status.HTTP_400_BAD_REQUEST)

