from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from api.models import Reservas
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.reservas_serializer import ReservasListSerializer, ReservasSerializer

#ViewSet del modelo reservas
class ReservasViewSet(viewsets.ModelViewSet):
    serializer_class = ReservasListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id_reserva', 'id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro', 'estado']
    search_fields = ['id_estudiante__doc_estudiante__doc', 'id_estudiante__nombres', 'id_estudiante__apellidos', 'ejemplares__id_libro__nombre', 'ejemplares__id_libro__isbn', 'ejemplares__id_libro__autores__nombres', 'ejemplares__id_libro__autores__apellidos', 'ejemplares__id_libro__categorias__nombre']
    ordering_fields = ['id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro__nombre','estado']

    def get_queryset(self, pk=None):
        if pk == None:
            return ReservasListSerializer.Meta.model.objects.all()
        return Reservas.objects.filter(id_reserva = pk).first()


    def create(self, request):
          serializer = ReservasSerializer(data = request.data)

          

          if serializer.is_valid():
              serializer.save()
              return Response({'data' : serializer.data, 'message':'Se ha agregado la reserva correctamente'}, status= status.HTTP_201_CREATED)
        
          return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        serializer = ReservasSerializer(reserva, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        reserva.delete()
        return Response({'message':'Reserva eliminada correctamente'}, status= status.HTTP_200_OK)