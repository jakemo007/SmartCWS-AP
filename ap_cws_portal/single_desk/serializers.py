# single_desk/serializers.py
from rest_framework import serializers

class BusinessLookupSerializer(serializers.Serializer):
    registration_number = serializers.CharField(
        max_length=50,
        required=True,
        help_text="Business registration number from Single Desk Portal"
    )
    
    def validate_registration_number(self, value):
        if not value.startswith('AP'):
            raise serializers.ValidationError("Registration number must start with 'AP'")
        return value