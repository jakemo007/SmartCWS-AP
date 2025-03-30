# compliance/serializers.py
from rest_framework import serializers
from .models import GIGWRequirement

class GIGWRequirementSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = GIGWRequirement
        fields = '__all__'
        read_only_fields = ('last_verified',)
    
    def get_status(self, obj):
        return "Implemented" if obj.is_implemented else "Pending"