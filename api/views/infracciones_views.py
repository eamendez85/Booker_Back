from django import views
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.infracciones_serializers import InfraccionesListSerializer, InfraccionesSerializer
from api.models import Ejemplares, Infracciones, Prestamos

#ViewSet del modelo Infracciones
class InfraccionesViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['id_tipo_infraccion','estado']
    search_fields = ['id_bibliotecario__doc_bibliotecario__doc', 'id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro__nombre', 'ejemplares__id_libro__isbn']
    ''' ordering_fields = ['ejemplares','id_tipo_infraccion','estado', 'id_bibliotecario', 'id_estudiante', 'ejemplares__id_libro']
 '''
    serializer_class = InfraccionesSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return InfraccionesListSerializer.Meta.model.objects.all()
        return Infracciones.objects.filter(id_infraccion = pk).first()

    def update(self, request, pk):
        infraccion = Infracciones.objects.filter(id_infraccion = pk).first()
        serializer = InfraccionesSerializer(infraccion, data = request.data)
        
        if serializer.is_valid():
            if request.data['estado'] == "C":
                prestamo_infraccion = infraccion.id_prestamo 
                prestamo_infraccion.estado="C"
                de_prestamo = prestamo_infraccion.id_de_prestamo
                de_prestamo.estado = "AC"
                ejemplar_prestamo = prestamo_infraccion.id_ejemplar
                ejemplar_prestamo.estado="D"
                prestamo_infraccion.save()
                ejemplar_prestamo.save() 
                de_prestamo.save()
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Infracción actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        infraccion = Infracciones.objects.filter(id_infraccion = pk).first()
        prestamo_infraccion = infraccion.id_prestamo 
        prestamo_infraccion.estado="C"
        ejemplar_prestamo = prestamo_infraccion.id_ejemplar
        ejemplar_prestamo.estado="D"
        prestamo_infraccion.save()
        ejemplar_prestamo.save() 
        infraccion.delete()
        return Response({'message':'Infracción eliminada correctamente'}, status= status.HTTP_200_OK)
