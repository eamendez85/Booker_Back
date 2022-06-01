from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from api.models import Ejemplares
from api.models import Infracciones
from api.models import Reservas
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.infracciones_serializers import InfraccionesListSerializer, InfraccionesSerializer
from api.serializers.reservas_serializer import ReservasListSerializer, ReservasSerializer

#ViewSet del modelo reservas
class ReservasViewSet(viewsets.ModelViewSet):
    serializer_class = ReservasSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id_reserva', 'id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro', 'estado']
    search_fields = ['id_estudiante__doc_estudiante__doc', 'id_estudiante__nombres', 'id_estudiante__apellidos', 'ejemplares__id_libro__nombre', 'ejemplares__id_libro__isbn', 'ejemplares__id_libro__autores__nombres', 'ejemplares__id_libro__autores__apellidos', 'ejemplares__id_libro__categorias__nombre']
    ordering_fields = ['id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro__nombre','estado']

    def get_queryset(self, pk=None):
        if pk == None:
            return ReservasListSerializer.Meta.model.objects.all()
        return Reservas.objects.filter(id_reserva = pk).first()

    def create(self, request):
        #Si un estudiante tiene una infracción que no pueda reservar un libro en la plataforma
        error_datos_reserva = {}
        estado_ejemplares={}
        validacion_estado_ejemplares=True
        id_estudiante = request.data.get('id_estudiante')
        estudiante_infraccion = Infracciones.objects.filter(id_estudiante = id_estudiante, estado="AV").first()
        ejemplares_reserva = request.data.get('ejemplares')

        reserva_serializer = ReservasSerializer(data = request.data)
        
        if estudiante_infraccion:
            return Response({'message':'El estudiante tiene una infracción vigente'}, status= status.HTTP_409_CONFLICT)
        else:
            for ejemplar_reserva in ejemplares_reserva:
                ejemplar = Ejemplares.objects.filter(id_ejemplar = ejemplar_reserva).first()
                if ejemplar.estado == "R":
                    validacion_estado_ejemplares=False
                    estado_ejemplares['ejemplar '+str(ejemplar_reserva)] = 'El ejemplar ya está reservado'
                elif ejemplar.estado == "IV":
                    validacion_estado_ejemplares=False
                    estado_ejemplares['ejemplar '+str(ejemplar_reserva)] = 'El ejemplar está inactivo'
                elif ejemplar.estado == "P":
                    validacion_estado_ejemplares=False
                    estado_ejemplares['ejemplar '+str(ejemplar_reserva)] = 'El ejemplar está prestado'
                elif ejemplar.estado == "INF":
                    validacion_estado_ejemplares=False
                    estado_ejemplares['ejemplar '+str(ejemplar_reserva)] = 'El ejemplar está en infracción'

                if validacion_estado_ejemplares:
                    ejemplar.estado = "R"
                    ejemplar.save()
            if validacion_estado_ejemplares:
                if reserva_serializer.is_valid():
                    reserva_serializer.save()
                    return Response({'data' : reserva_serializer.data, 'message':'Reserva creada correctamente'}, status= status.HTTP_201_CREATED)
                return Response(reserva_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            else:
                if not reserva_serializer.is_valid():
                    error_datos_reserva = reserva_serializer.errors
                return Response([estado_ejemplares, error_datos_reserva], status= status.HTTP_400_BAD_REQUEST)
            
    def update(self, request, pk):
        #Crear un registro de prestamo cuando el estado de una reserva pase a inactivo 
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        serializer = ReservasSerializer(reserva, data = request.data)
        
        
        if serializer.is_valid():
            estado = request.data.get('estado')
            if estado == "AC":
                print(estado)
                print("Actuaaaaal")
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)
            elif estado == "C":
                print(estado)
                print("Completadaaaa")
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)

            
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        reserva.delete()
        return Response({'message':'Reserva eliminada correctamente'}, status= status.HTTP_200_OK)