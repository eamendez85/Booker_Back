from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from api.models import Ejemplares
from api.models import Infracciones
from api.models import Reservas
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.infracciones_serializers import InfraccionesListSerializer, InfraccionesSerializer
from api.serializers.reservas_serializer import ReservasListSerializer, ReservasSerializer
from time import strftime, localtime
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()


#ViewSet del modelo reservas
class ReservasViewSet(viewsets.ModelViewSet):
    serializer_class = ReservasSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id_reserva', 'id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro', 'estado']
    search_fields = ['id_estudiante__doc_estudiante__doc', 'id_estudiante__nombres', 'id_estudiante__apellidos', 'ejemplares__id_libro__nombre', 'ejemplares__id_libro__isbn', 'ejemplares__id_libro__autores__nombres', 'ejemplares__id_libro__autores__apellidos', 'ejemplares__id_libro__categorias__nombre']
    ordering_fields = ['id_estudiante__doc_estudiante__doc', 'ejemplares__id_libro__nombre','estado', 'fecha_reserva', 'fecha_limite']

    #Cuando la fecha limite de una reserva termine que el estado de la reserva pase a inactivo y el ejemplar o ejemplares pasen a disponibles


    def get_queryset(self, pk=None):
        if pk == None:
            return ReservasListSerializer.Meta.model.objects.all()
        return Reservas.objects.filter(id_reserva = pk).first()

    def create(self, request):
        #El mutable sirve para poder agregar datos al request.data
        #Saco la fecha de reserva con el datetime.now que es la fecha cuando se cree la reserva
        #Y la fecha limite es la fecha de reserva con 3 dias sumados
        fecha_reserva = datetime.now()
        tiempo_limite = 1
        fecha_limite = fecha_reserva + timedelta(minutes= tiempo_limite)

        error_datos_reserva = {}
        estado_ejemplares={}

        validacion_estado_ejemplares=True
        id_estudiante = request.data.get('id_estudiante')
        estudiante_infraccion = Infracciones.objects.filter(id_estudiante = id_estudiante, estado="AV").first()
        #Este request de los ejemplares solo trae el ultimo ejemplar si son varios ejemplares
        ejemplares_reserva = request.data.get('ejemplares')

        request.data['fecha_reserva'] = fecha_reserva
        request.data['fecha_limite'] = fecha_limite

        print(fecha_reserva)
        print(fecha_limite)

        reserva_serializer = ReservasSerializer(data = request.data)

        #Si un estudiante tiene una infracción que no pueda reservar un libro en la plataforma
        if estudiante_infraccion:
            return Response({'message':'El estudiante tiene una infracción vigente'}, status= status.HTTP_409_CONFLICT)
        else:
            #Validaciones de ejemplares y sus estados
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
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        reserva.delete()
        return Response({'message':'Reserva eliminada correctamente'}, status= status.HTTP_200_OK)


    #Validación constante de si la fecha limite de reserva ya pasó o no, usando APScheduler, se le pone la validacion cada 1 segundo
    @scheduler.scheduled_job('interval', seconds=1)
    def validacion_fecha_reserva():
        reservas = Reservas.objects.filter()
        for reserva in reservas:
            if reserva.reserva_cancelada_por_fecha_limite == True:
                ejemplares = reserva.ejemplares.filter()
                for ejemplar in ejemplares:
                    if reserva.estado == "AC":
                        ejemplar.estado = "D"
                        ejemplar.save()
                reserva.estado = "IV"
                reserva.save()
            else:
                pass

    scheduler.start()