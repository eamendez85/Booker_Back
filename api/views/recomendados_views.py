from rest_framework import viewsets
from api.models import Libros
from api.serializers.libros_serializers import LibrosListSerializer
from api.serializers.recomendados_serializers import RecomendadosListSerializer

class RecomendadosViewSet(viewsets.ModelViewSet):
    serializer_class = LibrosListSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            libros = Libros.objects.filter(estado = "I")
            return LibrosListSerializer.Meta.model.objects.filter(id_libro = 1) | LibrosListSerializer.Meta.model.objects.filter(id_libro = 2 )
        return LibrosListSerializer.objects.filter(id_libro = pk).first()