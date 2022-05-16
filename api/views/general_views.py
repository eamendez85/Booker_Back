from django import views
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers.ejemplares_serializers import EjemplaresSerializer, EjemplaresListSerializer
from api.serializers.infracciones_serializers import InfraccionesListSerializer, InfraccionesSerializer
from api.models import Autores, Categorias, DePrestamos, Editoriales, Ejemplares, Favoritos, Grados, Grupos, Idiomas, Infracciones, Reservas, TipoInfraccion
from api.serializers.general_serializers import AutoresSerializer, CategoriasSerializer, EditorialesSerializer, GradosSerializer, GruposSerializer, IdiomasSerializer,  PrestadosSerializer, TipoInfraccionesSerializer
from api.authentication_mixins import Authentication
from api.serializers.detalles_prestamo_serializer import DetallePrestamosSerializer, DetallePrestamosListSerializer
from api.serializers.favoritos_serializers import FavoritosListSerializer, FavoritosSerializer
from api.serializers.reservas_serializer import ReservasListSerializer, ReservasSerializer


#Viewset del modelo grados
class GradoViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = GradosSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return GradosSerializer.Meta.model.objects.all()
        return Grados.objects.filter(id_grado = pk).first()
        

#ViewSet del modelo grupos
class GruposViewSet(viewsets.ModelViewSet):
    serializer_class = GruposSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return GruposSerializer.Meta.model.objects.all()
        return Grupos.objects.filter(id_grupo = pk).first()

    def create(self, request):
        serializer = GruposSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Se ha creado el grupo correctamente'}, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        grupo = Grupos.objects.filter(id_grupo = pk).first()
        serializer = GruposSerializer(grupo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Grupo actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        grupo = Grupos.objects.filter(id_grupo = pk).first()
        grupo.delete()
        return Response({'message':'Grupo eliminado correctamente'}, status= status.HTTP_200_OK)
        

#ViewSet del modelo categorias
class CategoriasViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['nombre']
    search_fields = ['nombre']
    ordering_fields = ['nombre']


    serializer_class = CategoriasSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return CategoriasSerializer.Meta.model.objects.all()
        return Categorias.objects.filter(id_categoria = pk).first()

    def create(self, request):
            serializer = CategoriasSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado la categoria correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        categoria = Categorias.objects.filter(id_categoria = pk).first()
        serializer = CategoriasSerializer(categoria, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Categoria actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        categoria = Categorias.objects.filter(id_categoria = pk).first()
        categoria.delete()
        return Response({'message':'Categoria eliminada correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo autores
class AutoresViewset(viewsets.ModelViewSet):
    serializer_class = AutoresSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return AutoresSerializer.Meta.model.objects.all()
        return Autores.objects.filter(id_autor = pk).first()

    def create(self, request):
            serializer = AutoresSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado el autor correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        autor = Autores.objects.filter(id_autor = pk).first()
        serializer = AutoresSerializer(autor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Autor actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        autor = Autores.objects.filter(id_autor = pk).first()
        autor.delete()
        return Response({'message':'Autor eliminado correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo editoriales
class EditorialesViewSet(viewsets.ModelViewSet):
    serializer_class = EditorialesSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return EditorialesSerializer.Meta.model.objects.all()
        return Editoriales.objects.filter(id_editorial = pk).first()

    def create(self, request):
            serializer = EditorialesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha creado la editorial correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        editorial = Editoriales.objects.filter(id_editorial = pk).first()
        serializer = EditorialesSerializer(editorial, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Editorial actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        editorial = Editoriales.objects.filter(id_editorial = pk).first()
        editorial.delete()
        return Response({'message':'Editorial eliminada correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo idiomas
class IdiomasViewSet(viewsets.ModelViewSet):
    serializer_class = IdiomasSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return IdiomasSerializer.Meta.model.objects.all()
        return Idiomas.objects.filter(id_idioma = pk).first()

    def create(self, request):
            serializer = IdiomasSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha agregado el idioma correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        idioma = Idiomas.objects.filter(id_idioma = pk).first()
        serializer = IdiomasSerializer(idioma, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Idioma actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        idioma = Idiomas.objects.filter(id_idioma = pk).first()
        idioma.delete()
        return Response({'message':'Idioma eliminado correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo Favoritos
class FavoritosViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritosListSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return FavoritosListSerializer.Meta.model.objects.all()
        return Favoritos.objects.filter(id_favorito = pk).first()

    def create(self, request):
            serializer = FavoritosSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha agregado el libro favorito correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        favorito = Favoritos.objects.filter(id_favorito = pk).first()
        serializer = EjemplaresSerializer(favorito, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Libro favorito actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        favorito = Favoritos.objects.filter(id_favorito = pk).first()
        favorito.delete()
        return Response({'message':'Libro favorito eliminado correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo ejemplares
class EjemplaresViewSet(viewsets.ModelViewSet):
    serializer_class = EjemplaresListSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return EjemplaresListSerializer.Meta.model.objects.all()
        return Ejemplares.objects.filter(id_ejemplar = pk).first()

    def create(self, request):
            serializer = EjemplaresSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha agregado el ejemplar correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        ejemplar = Ejemplares.objects.filter(id_ejemplar = pk).first()
        serializer = EjemplaresSerializer(ejemplar, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Ejemplar actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        ejemplar = Ejemplares.objects.filter(id_ejemplar = pk).first()
        ejemplar.delete()
        return Response({'message':'Ejemplar eliminado correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo tipoInfraccion
class TipoInfraccionViewSet(viewsets.ModelViewSet):
    serializer_class = TipoInfraccionesSerializer
    def get_queryset(self, pk=None):
        if pk == None:
            return TipoInfraccionesSerializer.Meta.model.objects.all()
        return TipoInfraccion.objects.filter(id_tipo_infraccion = pk).first()

#ViewSet del modelo Infracciones
class InfraccionesViewSet(viewsets.ModelViewSet):
    serializer_class = InfraccionesListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['id_estudiante__doc_estudiante', 'ejemplares','id_tipo_infraccion__nombre','estado','id_administrador__doc_bibliotecario']
    search_fields = ['id_estudiante__doc_estudiante', 'ejemplares','id_tipo_infraccion__nombre','estado','id_administrador__doc_bibliotecario']
    ordering_fields = ['id_estudiante__doc_estudiante', 'ejemplares','id_tipo_infraccion__nombre','estado','id_administrador__doc_bibliotecario']


    def get_queryset(self, pk=None):
        if pk == None:
            return InfraccionesListSerializer.Meta.model.objects.all()
        return Infracciones.objects.filter(id_infraccion = pk).first()

    def create(self, request):
            serializer = InfraccionesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha agregado la infracción al estudiante correctamente'}, status= status.HTTP_201_CREATED)
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        infraccion = Infracciones.objects.filter(id_infraccion = pk).first()
        serializer = InfraccionesSerializer(infraccion, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Infracción actualizada correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        infraccion = Infracciones.objects.filter(id_infraccion = pk).first()
        infraccion.delete()
        return Response({'message':'Infracción eliminada correctamente'}, status= status.HTTP_200_OK)

#ViewSet del modelo Detalles prestamos
class DetallePrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = DetallePrestamosListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields= ['id_estudiante__doc_estudiante', 'ejemplares','fec_prestamo','fec_devolucion','estado','id_administrador__doc_bibliotecario']
    search_fields = ['id_estudiante__doc_estudiante', 'ejemplares','fec_prestamo','fec_devolucion','estado','id_administrador__doc_bibliotecario']
    ordering_fields = ['id_estudiante__doc_estudiante', 'ejemplares','fec_prestamo','fec_devolucion','estado','id_administrador__doc_bibliotecario']



    def get_queryset(self, pk=None):
        if pk == None:
            return DetallePrestamosListSerializer.Meta.model.objects.all()
        return DePrestamos.objects.filter(id_de_prestamo = pk).first()

    def create(self, request):
            serializer = DetallePrestamosSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Se ha agregado el prestamo al estudiante correctamente'}, status= status.HTTP_201_CREATED)
            
            serializer_prestados = PrestadosSerializer(data = request.data)
            if serializer_prestados.is_valid():
                serializer_prestados.save()
                print("Prestado guardado")
        
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        detalle_prestamo = DePrestamos.objects.filter(id_de_prestamo = pk).first()
        serializer = DetallePrestamosSerializer(detalle_prestamo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message':'Prestamo actualizado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        detalle_prestamo = DePrestamos.objects.filter(id_de_prestamo = pk).first()
        detalle_prestamo.delete()
        return Response({'message':'Registro de prestamo eliminado correctamente'}, status= status.HTTP_200_OK)


#ViewSet del modelo reservas
class ReservasViewSet(viewsets.ModelViewSet):
    serializer_class = ReservasListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields= ['id_estudiante__doc_estudiante', 'ejemplares','estado']
    search_fields = ['id_estudiante__doc_estudiante', 'ejemplares','estado']
    ordering_fields = ['id_estudiante__doc_estudiante', 'ejemplares','estado']

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


#Intento de update borrando registro de reserva y creando uno de prestamo
'''     def update(self, request, pk):
        reserva = Reservas.objects.filter(id_reserva = pk).first()
        serializer = ReservasSerializer(reserva, data = request.data)
        if Reservas.estado == "a":
            if serializer.is_valid():
                serializer.save()
                return Response({'data' : serializer.data, 'message':'Reserva actualizada correctamente'}, status= status.HTTP_200_OK)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        elif Reservas.estado == "i":
            serializer_prestamo = DetallePrestamosSerializer(data = request.data)
            if serializer_prestamo.is_valid():
                serializer_prestamo.save()
                return Response({'data' : serializer_prestamo.data, 'message':'Su reserva ha pasado a prestamo satisfactoriamente'}, status= status.HTTP_200_OK)
 '''

