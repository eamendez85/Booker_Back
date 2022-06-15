from distutils.command.upload import upload
from rest_framework import serializers

class CsvSerializer(serializers.Serializer):
    csv = serializers.FileField(use_url="/csv_estudiantes/")
    
    