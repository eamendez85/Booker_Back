from api.serializers.eventos_serializers import EventosListSerializer, EventosSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.response import Response

class EventosViewSet(viewsets.ModelViewSet):

    serializer_class = EventosListSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return EventosListSerializer.Meta.model.objects.all()
        return EventosListSerializer.objects.filter(id_grado = pk).first()

    def create(self, request):
        serializer = EventosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Se ha creado el evento correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)