from rest_framework import viewsets
from api.serializers.detalles_prestamo_serializer import PrestamosListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters

class PrestamosViewset(viewsets.ModelViewSet):
  
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['estado', 'id_ejemplar__id_libro__id_libro']
    ordering_fields = ['fec_devolucion'] 

    serializer_class = PrestamosListSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return PrestamosListSerializer.Meta.model.objects.all()
        return PrestamosListSerializer.objects.filter(id_prestamo = pk).first()