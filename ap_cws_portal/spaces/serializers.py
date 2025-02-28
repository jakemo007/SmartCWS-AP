from rest_framework import serializers
from .models import CoworkingSpace

class CoworkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpace
        fields = '__all__'
