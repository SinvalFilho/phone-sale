from rest_framework import serializers
from .models import Celular

class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'
