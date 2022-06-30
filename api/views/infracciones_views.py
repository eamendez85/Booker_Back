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
    
    filterset_fields= ['id_tipo_infraccion', 'id_estudiante__id_estudiante','estado']
    search_fields = ['id_bibliotecario__doc_bibliotecario', 'id_estudiante__doc_estudiante', 'id_prestamo__id_ejemplar__id_libro__nombre', 'id_prestamo__id_ejemplar__id_libro__isbn', 'id_estudiante__nombres', 'id_estudiante__apellidos']
    ordering_fields = ['ejemplares','id_tipo_infraccion', 'id_infraccion']

    serializer_class = InfraccionesListSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return InfraccionesListSerializer.Meta.model.objects.all()
        return Infracciones.objects.filter(id_infraccion = pk).first()
    def update(self, request, pk):
        infraccion = Infracciones.objects.filter(id_infraccion = pk).first()
        serializer = InfraccionesSerializer(infraccion, data = request.data)
        
        if serializer.is_valid():
            prestamo_infraccion = infraccion.id_prestamo
            de_prestamo = prestamo_infraccion.id_de_prestamo
            ejemplar_prestamo = prestamo_infraccion.id_ejemplar

            if request.data['estado'] == "C":
                cant_completados = 0
                de_prestamo_inf = False
                prestamo_infraccion.estado="C"
                prestamo_infraccion.save()
                ejemplar_prestamo.estado="D"
                prestamos = Prestamos.objects.filter(id_de_prestamo = de_prestamo)
                for prestamo in prestamos:
                    if prestamo.estado == "C":
                        cant_completados+=1
                    elif prestamo.estado == "INF":
                        de_prestamo_inf = True

                if len(prestamos)==cant_completados:
                    de_prestamo.estado = "C"
                elif de_prestamo_inf:
                    de_prestamo.estado = "INF"
                else:
                    de_prestamo.estado = "AC"
                ejemplar_prestamo.save() 
                de_prestamo.save()

            elif request.data['estado'] == "AV":
                prestamo_infraccion.estado="INF"
                de_prestamo.estado = "INF"
                ejemplar_prestamo.estado="INF"
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
