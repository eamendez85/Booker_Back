from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    
    #Calculo del dia de expiracion
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        
        return left_time
    
    #Verifica si el token a expirado
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds= 0)
    
    #Retorna si el token esta expirado
    def token_expire_handle(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user= token.user
            token.delete()
            #Refresca el token
            token = self.get_model().objects.create(user = user)
            
        return is_expire, token
    
    
    #Sobreescribiendo metodo para agregar la expiracion
    def authenticate_credentials(self, key):
        message, token,user = None, None,None
        
        try:
            token=self.get_model().objects.select_related('user').get(key=key)
            user=token.user
            
        except self.get_model().DoesNotExist:
            
            message = 'Token invalido.'
            self.expired = True
        
        if token is not None:
            print("USUARIO ACTIVO: ", token.user.usuario_activo)
            if not token.user.usuario_activo:
                message = 'Usuario no activo o eliminado.'
        
            is_expired,token = self.token_expire_handle(token)
            if is_expired:
                message = 'Su Token ha expirado.'
                
            print("MENSAJE: ",message)
                
        return (user, token, message, self.expired)