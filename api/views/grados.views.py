from telnetlib import STATUS
from requests import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.models import Grados
from api.serializers.grados_serializers import GradosSerializer

class GradoViewSet(viewsets.ModelViewSet):
    serializerClass = GradosSerializer
    queryset = GradosSerializer.Meta.model.objects

@api_view(['GET', 'POST'])
def grado_api_view(request):

    #listar grados
    if request.method == 'GET':
        #queryset
        grados = Grados.objects.all()
        serializer = GradosSerializer(grados, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    #agregar grados
    elif request.method == 'POST':
        serializer = GradosSerializer(data = request.data)
        #validacion para despues guardar el grado
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Se ha creado el grado correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#pk es la primary key que se va a recibir para consultar el objeto unico
@api_view(['GET', 'PUT', 'DELETE'])
def grado_detail(request, pk):
    #queryset
    grado = Grados.objects.filter(id_grado = pk).first()

    #validacion
    if grado:
        #metodo obtener por id
        if request.method == 'GET':
            serializer = GradosSerializer(grado)
            return Response(serializer.data, status= status.HTTP_200_OK)

        #metodo actualizar grado
        elif request.method == 'PUT':
            serializer = GradosSerializer(grado, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        #metodo borrar grado
        elif request.method == 'DELETE':          
            grado.delete()
            return Response({'message':'Grado eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'message': 'No se ha encontrado un grado con ese id'}, status= status.HTTP_404_NOT_FOUND)


