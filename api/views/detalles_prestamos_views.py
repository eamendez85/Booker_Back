from warnings import catch_warnings
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import TipoInfraccion
from api.models import DePrestamos, Prestamos, Estudiantes, Ejemplares, Infracciones
from rest_framework import status, filters
from api.serializers.detalles_prestamo_serializer import DetallePrestamosListSerializer, DetallePrestamosSerializer, PrestamosSerializer
from api.serializers.infracciones_serializers import InfraccionesSerializer, InfraccionesListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

#ViewSet del modelo Detalles prestamos
class DetallePrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = DetallePrestamosListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['estado']
    search_fields = ['id_estudiante__doc_estudiante__doc', 'id_bibliotecario__doc_bibliotecario__doc','prestamos__id_ejemplar__id_libro__isbn', 'prestamos__id_ejemplar__id_libro__nombre']
    ordering_fields = ['fec_prestamo', 'prestamos__fec_devolucion']

    def get_queryset(self, pk=None):
        if pk == None:
            return DetallePrestamosListSerializer.Meta.model.objects.all()
        return DePrestamos.objects.filter(id_de_prestamo = pk).first()
    
    def create(self, request):
        errors={}
        error=False
        prestamos_data = request.data.get('prestamos')
        fecha_prestamo = date.today()
        request.data['fec_prestamo'] = fecha_prestamo
        request.data.pop('prestamos')
        de_prestamo_serializer = DetallePrestamosSerializer(data = request.data)
        
        
        if de_prestamo_serializer.is_valid():
            de_prestamo_serializer.save()
            id_de_prestamo = de_prestamo_serializer.data.get("id_de_prestamo")
        else:
            error=True
            errors['detalles_prestamo']=de_prestamo_serializer.errors
        
        #Agregar id_de_pretamo a cada prestamo
        for prestamo in prestamos_data:
            
            #CAmbiar estado a prestado de ejemplar
            ejemplar =  Ejemplares.objects.filter(id_ejemplar = prestamo.get('id_ejemplar')).first()
            ejemplar.estado = "P"
            ejemplar.save()
            try: 
                prestamo['id_de_prestamo']=id_de_prestamo
            except:
                pass
        prestamos_serializer = PrestamosSerializer(data = prestamos_data, many=True)
        
        if prestamos_serializer.is_valid():
            prestamos_serializer.save()
            if error == False:
                return Response({'message':'Se ha creado el prestamo correctamente'}, status= status.HTTP_201_CREATED)
        else:
            errors['prestamos']=prestamos_serializer.errors
        return Response(errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        errors={}
        error=False
        counter=0
        de_prestamo_inf = False
        prestamo_request={}
        prestamos_request=request.data.get('prestamos')
        de_prestamo = DePrestamos.objects.filter(id_de_prestamo = pk).first()
        prestamos = Prestamos.objects.filter(id_de_prestamo = pk)
        
        if request.data.get('estado') == "C":
            for prestamo_request in prestamos_request:
                ejemplar = Ejemplares.objects.filter(id_ejemplar = prestamo_request['id_ejemplar']).first()
                ejemplar.estado = "D"
                ejemplar.save()
                
            for prestamo in prestamos:
                prestamo_request = request.data.get('prestamos')[counter]
                prestamo_request['estado'] = "C"
                prestamo_serializer = PrestamosSerializer(prestamo, prestamo_request)
                counter+=1
                if prestamo_serializer.is_valid():
                    prestamo_serializer.save()
                else:
                    error=True
                    errors['prestamo '+ str(counter)]=prestamo_serializer.errors
        else:
            for prestamo_request in prestamos_request:
                if prestamo_request['estado'] == "C":
                    ejemplar = Ejemplares.objects.filter(id_ejemplar = prestamo_request['id_ejemplar']).first()
                    ejemplar.estado = "D"
                    ejemplar.save()
                elif prestamo_request['estado'] == "INF":
                    de_prestamo_inf = True
                    ejemplar = Ejemplares.objects.filter(id_ejemplar = prestamo_request['id_ejemplar']).first()
                    ejemplar.estado = "INF"
                    ejemplar.save()
                    id_estudiante_prestamo = de_prestamo.id_estudiante.id_estudiante
                    estudiante = Estudiantes.objects.get(id_estudiante = id_estudiante_prestamo)
                    fecha_actual = date.today()
                    #Al actualizar el prestamo se tiene que poner en la data el id del prestamo
                    prestamo = Prestamos.objects.filter(id_prestamo = prestamo_request['id_prestamo']).first()
                    infraccion_prestamo = Infracciones(id_estudiante = estudiante, id_prestamo = prestamo, fecha_infraccion = fecha_actual, estado = 'AV')
                    infraccion_prestamo.save()

                elif prestamo_request['estado'] == "AC":
                    ejemplar = Ejemplares.objects.filter(id_ejemplar = prestamo_request['id_ejemplar']).first()
                    ejemplar.estado = "P"
                    ejemplar.save()

            for prestamo in prestamos:
                prestamo_serializer = PrestamosSerializer(prestamo, data = request.data.get('prestamos')[counter])
                counter+=1
                if prestamo_serializer.is_valid():
                    prestamo_serializer.save()
                else:
                    error=True
                    errors['prestamo '+ str(counter)]=prestamo_serializer.errors
        
        request.data.pop('prestamos')
        if de_prestamo_inf:
            request.data['estado']="INF"
        de_prestamo_serializer= DetallePrestamosSerializer(de_prestamo, data = request.data)
            
        if de_prestamo_serializer.is_valid():
            de_prestamo_serializer.save()
            if error == False:
                return Response({'message':'El prestamo se ha actualizado correctamente'}, status= status.HTTP_200_OK)
        else:
            errors['detalles_prestamo']=de_prestamo_serializer.errors
        
        return Response(errors, status= status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        de_prestamo = DePrestamos.objects.filter(id_de_prestamo = pk).first()
        prestamos = Prestamos.objects.filter(id_de_prestamo = pk)
        for prestamo in prestamos:
            ejemplar = Ejemplares.objects.filter(id_ejemplar = prestamo.id_ejemplar.id_ejemplar).first()
            ejemplar.estado = "D"
            ejemplar.save()
            prestamo.delete()
        de_prestamo.delete()
        return Response({'message':'Prestamo eliminado correctamente'}, status= status.HTTP_200_OK)

    @scheduler.scheduled_job('interval', seconds=60)
    def validacion_infraccion_fec_devolucion():
        #Cuando el prestamo pase de la fecha de devolucion y esté en estado AC, 
        # que se cree una infracción de ese estudiante, que el estado del prestamo pase a infraccion 
        #y que el estado del ejemplar pase a infracción
        detalle_prestamos = DePrestamos.objects.filter()
        for de_prestamo in detalle_prestamos:
            prestamos = de_prestamo.prestamos.filter()
            for prestamo in prestamos:
                if prestamo.fec_devolucion == None:
                    pass
                else:
                    if prestamo.infraccion_prestamo_por_fecha_devolucion == True and prestamo.estado == "AC": 
                        prestamo.estado = "INF"
                        
                        if prestamo.estado == "INF":
                            #Datos para la infracción
                            id_estudiante_prestamo = de_prestamo.id_estudiante.id_estudiante
                            estudiante = Estudiantes.objects.get(id_estudiante = id_estudiante_prestamo)
                            id_ejemplar_prestamo = prestamo.id_ejemplar.id_ejemplar
                            ejemplar = Ejemplares.objects.get(id_ejemplar = id_ejemplar_prestamo)
                            tipo_infraccion = TipoInfraccion.objects.get(id_tipo_infraccion = "2")
                            #Se crea la infracción
                            infraccion_estudiante = Infracciones(id_estudiante = estudiante, id_ejemplar = ejemplar, id_tipo_infraccion = tipo_infraccion, estado= "AV")
                            infraccion_estudiante.save()

                            #Cambio el estado de los ejemplares
                            ejemplar.estado = "INF"
                            ejemplar.save()
                        prestamo.save()
                    elif prestamo.infraccion_prestamo_por_fecha_devolucion == True and prestamo.estado == "C":   
                        pass
                    else:
                        pass
    scheduler.start()
