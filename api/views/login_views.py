#cerrar todas las sesiones al inicar sesion
from django.contrib.sessions.models import Session
from datetime import datetime
from django.utils import timezone

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from api.models import Administradores, Estudiantes
from api.serializers.usuarios_serializers import AdministradoresListSerializer, EstudiantesListSerializer
from api.serializers.usuarios_serializers import UsuariosListSerializer

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
                token,created = Token.objects.get_or_create(user = user)
                if user.usuario_administrador:
                    administrador = Administradores.objects.filter(doc_administrador=user.doc).first()
                    user_serializer = AdministradoresListSerializer(administrador)
                elif user.usuario_administrador==False:
                    estudiante = Estudiantes.objects.filter(doc_estudiante = user.doc).first()
                    user_serializer = EstudiantesListSerializer(estudiante)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
                else:
                    #cerrar todas las sesiones al inicar sesion
                    """
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.doc == int(session_data.get('_auth_user_id')):
                                session.delete()
                    """         
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
            

class Logout(APIView):
    
    def get(self, request, *args, **kwargs):

        """
        logout - Cerrar sesion

        Recibe parametro 'token' por peticion HTTP GET
        """

        token = Token.objects.filter(key = request.GET.get('token')).first()
            
        if token:
            user = token.user
                
            all_sessions = Session.objects.filter(expire_date__gte = timezone.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if int(user.doc) == int(session_data['_auth_user_id']):
                        session.delete()
                
            token.delete()
                
            session_message = 'Sesiones de usuario eliminados.'
            token_message = 'Token eliminado.'
            return Response({'token_message':token_message, 'session_message':session_message}, status = status.HTTP_200_OK)
            
        return Response({'error':'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
                
                
        
"""
Autorizacion
Recibe por Headers

key = 'Authorization'
value = 'Token sasd25255dasrdfsadasd'
"""