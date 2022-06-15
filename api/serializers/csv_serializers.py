from rest_framework import serializers
from api.models import CsvEstudiantes

class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = CsvEstudiantes
        fields = '__all__'