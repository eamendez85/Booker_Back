from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from api.models import DePrestamos, Ejemplares, Estudiantes, Prestamos
from api.models import Infracciones
from api.models import Reservas
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.infracciones_serializers import InfraccionesListSerializer, InfraccionesSerializer
from api.serializers.reservas_serializer import ReservasListSerializer, ReservasSerializer
from datetime import timedelta, date
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 1})


#ViewSet del modelo reservas
class ReservasViewSet(viewsets.ModelViewSet):
    serializer_class = ReservasListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id_reserva', 'id_estudiante__doc_estudiante__doc', 'id_estudiante__id_estudiante','ejemplares__id_libro', 'estado']
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
        fecha_reserva = date.today()
        error_datos_reserva = {}
        estado_ejemplares={}
        validacion_estado_ejemplares=True
        prestamos_ac_estudiante = []
        prestamos_filtrados = []
        total_ejem_reservados = 0
        
        fecha_limite = fecha_reserva + timedelta(days=1)

        #Datos de validacion de estudiante
        id_estudiante = request.data.get('id_estudiante')
        estudiante_infraccion = Infracciones.objects.filter(id_estudiante = id_estudiante, estado="AV").first()
        reservas_ac_estudiante = Reservas.objects.filter(id_estudiante = id_estudiante, estado = "AC")
        for reserva in reservas_ac_estudiante:
            total_ejem_reservados+=len(reserva.ejemplares.all())
            
        print("TOTAL EJEMPLARES RESERVADOS", total_ejem_reservados)
        de_prestamos_estudiante = DePrestamos.objects.filter(id_estudiante = id_estudiante)
        for objecto in de_prestamos_estudiante:
            prestamos_filtrados = Prestamos.objects.filter(id_de_prestamo = objecto.id_de_prestamo, estado = "AC")
            if prestamos_filtrados:
                for prestamo_filtrado in prestamos_filtrados: 
                    prestamos_ac_estudiante.append(prestamo_filtrado)

        total_ejemplares_estudiante = total_ejem_reservados+ len(prestamos_ac_estudiante)

        #Este request de los ejemplares solo trae el ultimo ejemplar si son varios ejemplares
        ejemplares_reserva = request.data.get('ejemplares')

        request.data['fecha_reserva'] = fecha_reserva
        request.data['fecha_limite'] = fecha_limite

        reserva_serializer = ReservasSerializer(data = request.data)

        #Si un estudiante tiene una infracción que no pueda reservar un libro en la plataforma
        if estudiante_infraccion:
            return Response({'message':'El estudiante tiene una infracción vigente'}, status= status.HTTP_409_CONFLICT)
        elif (total_ejemplares_estudiante >= 3):
            return Response({'message':'El estudiante ha superado al limite de ejemplares prestados o reservados (3)'}, status= status.HTTP_401_UNAUTHORIZED)
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
        validacion_err_ejemplares = False
        #Crear un registro de prestamo cuando el estado de una reserva pase a inactivo 
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        reservas_serializer = ReservasSerializer(reserva, data = request.data)
        ejemplares=request.data.get('ejemplares')
        
        
        if reservas_serializer.is_valid():
            estado = request.data.get('estado')
            if estado == "AC":
                reservas_serializer.save()
                return Response({'data' : reservas_serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)
            elif estado == "C":
                #Creacion de prestamo
                errores_ejemplares = {}
                ejemplares_prestamos = {}
                data_front ={}

                #Creacion detalles de prestamo
                estudiante = Estudiantes.objects.filter(id_estudiante = request.data.get('id_estudiante')).first()
                de_prestamo = DePrestamos(id_estudiante = estudiante, fec_prestamo = date.today(), estado="AC")
                
                #Creacion de prestamos
                for id_ejemplar in ejemplares:
                    ejemplar = Ejemplares.objects.filter(id_ejemplar = id_ejemplar).first()
                    if ejemplar.estado == "R":
                        ejemplar.estado = "P"
                        ejemplares_prestamos['ejemplar '+ str(id_ejemplar)]=ejemplar
                    else:
                        validacion_err_ejemplares = True
                        errores_ejemplares['ejemplar '+ str(id_ejemplar)]='No se encuentra reservado'
                
                if validacion_err_ejemplares:
                    return Response(errores_ejemplares, status=status.HTTP_409_CONFLICT)
                else:
                    de_prestamo.save()
                    #data_front['id_de_prestamo']=de_prestamo.id_de_prestamo
                    for key in ejemplares_prestamos:
                        value = ejemplares_prestamos[key]
                        value.save()
                        prestamo = Prestamos(id_de_prestamo = de_prestamo, id_ejemplar = value, estado = "AC")
                        prestamo.save()
                    reservas_serializer.save()
                    #data_front['data_reserva']=
                    return Response({'data' : reservas_serializer.data, 'id_de_prestamo':de_prestamo.id_de_prestamo,'message':'Se ha actualizado la reserva y se ha creado el prestamo'}, status= status.HTTP_200_OK)
                
            elif estado == "IV":
                ejemplares_disponibles = {}
                for id_ejemplar in ejemplares:
                    ejemplar = Ejemplares.objects.filter(id_ejemplar = id_ejemplar).first()
                    if ejemplar.estado == "R":
                        ejemplar.estado = "D"
                        ejemplares_disponibles['ejemplar '+ str(id_ejemplar)]=ejemplar
                    else:
                        validacion_err_ejemplares = True
                        errores_ejemplares['ejemplar '+ str(id_ejemplar)]='No se encuentra reservado'
                
                if validacion_err_ejemplares:
                    return Response(errores_ejemplares, status=status.HTTP_409_CONFLICT)
                else:
                    for key in ejemplares_disponibles:
                        value = ejemplares_disponibles[key]
                        value.save()
                    reservas_serializer.save()
                    return Response({'data' : reservas_serializer.data, 'message':'Se ha actualizado la reserva correctamente'}, status= status.HTTP_200_OK)
            
        return Response(reservas_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        for ejemplar in reserva.ejemplares.all():
            ejemplar.estado = "D"
            ejemplar.save()
        reserva.delete()
        return Response({'message':'Reserva eliminada correctamente'}, status= status.HTTP_200_OK)


    #Validación constante de si la fecha limite de reserva ya pasó o no, usando APScheduler, se le pone la validacion cada 1 segundo
    @scheduler.scheduled_job('interval', seconds=60)
    def validacion_fecha_reserva():
        reservas = Reservas.objects.filter()
        for reserva in reservas:
            if reserva.fecha_limite == None:
                pass
            else:
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