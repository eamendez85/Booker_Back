from rest_framework import serializers
from api.models import Eventos
from api.serializers.usuarios_serializers import BibliotecariosInformacionGeneralSerializer

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'

class EventosListSerializer(serializers.ModelSerializer):

  id_bibliotecario = BibliotecariosInformacionGeneralSerializer(many = False, read_only=True)

  class Meta:
        model = Eventos
        fields = ['id_evento', 'descripcion', 'imagen_evento', 'titulo', 'fec_inicio', 'fec_fin', 'estado', 'id_bibliotecario']