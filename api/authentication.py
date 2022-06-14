from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    
    #Calculo del dia de expiracion
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        
        return left_time
    
    #Verifica si el token a expirado
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds= 0)
    
    #Retorna si el token esta expirado
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            user= token.user
            token.delete()
            #Refresca el token
            token = self.get_model().objects.create(user = user)
            
        return token
    
    
    #Sobreescribiendo metodo para agregar la expiracion
    def authenticate_credentials(self, key):
        user = None
        
        try:
            token=self.get_model().objects.select_related('user').get(key=key)
            token = self.token_expire_handler(token)
            user = token.user
        except self.get_model().DoesNotExist:
            pass
                
        return user