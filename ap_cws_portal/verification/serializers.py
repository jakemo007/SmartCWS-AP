from rest_framework import serializers
from .models import SpaceVerification

class SpaceVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceVerification
        fields = '__all__'
