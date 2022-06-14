from rest_framework import serializers
from api.models import Libros
from api.serializers.libros_serializers import LibrosListSerializer

class RecomendadosListSerializer(serializers.ModelSerializer):

  libro = LibrosListSerializer(many=False, read_only=True)

  class Meta:
        model = Libros
        fields = ['libro']