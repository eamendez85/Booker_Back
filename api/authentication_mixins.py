from rest_framework.authentication import get_authorization_header

from api.authentication import ExpiringTokenAuthentication

class Authentication(object):
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            print(token)
        return None
    
    #Metodo que toda clase django ejecuta primero
    def dispatch(self, request, *args, **kwargs):
        
        user = get_user(request)
        
        return super().dispatch(request, *args, **kwargs)
    