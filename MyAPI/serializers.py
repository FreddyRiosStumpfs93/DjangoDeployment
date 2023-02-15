from rest_framework import serializers
from .models import clasificacion

class clasificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = clasificacion
        fields = '__all__'