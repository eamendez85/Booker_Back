from rest_framework import status
from rest_framework.response import Response
from api.models import Bibliotecarios, Estudiantes, Usuario
from api.serializers.usuarios_serializers import BibliotecariosListSerializer, EstudiantesListSerializer, UsuariosSerializer
from api.serializers.usuarios_serializers import UsuariosListSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):

        """
        Login - Inicar sesion

        Recibe un form-data {'username':'', 'password':''}
        """

        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.usuario_activo:
                if user.tipo_usuario == 'B':
                    bibliotecario = Bibliotecarios.objects.filter(doc_bibliotecario=user.doc).first()
                    user_serializer = BibliotecariosListSerializer(bibliotecario)
                elif user.tipo_usuario=='E':
                    estudiante = Estudiantes.objects.filter(doc_estudiante = user.doc).first()
                    user_serializer = EstudiantesListSerializer(estudiante)
                elif user.tipo_usuario=='A':
                    usuario = Usuario.objects.filter(doc = user.doc).first()
                    user_serializer = UsuariosListSerializer(usuario)

                return Response({
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)