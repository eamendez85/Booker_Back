from attr import fields
from django.forms import ValidationError
from rest_framework import serializers
from api.models import Grados

class GradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grados
        fields = '__all__'
