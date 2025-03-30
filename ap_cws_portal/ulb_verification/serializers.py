from rest_framework import serializers
from .models import ULBVerification

class ULBVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ULBVerification
        fields = ['id', 'space', 'status', 'comments', 'verified_by', 'verification_date']
        read_only_fields = ['id', 'verified_by', 'verification_date']

    def validate(self, data):
        if data.get('status') == 'rejected' and not data.get('comments'):
            raise serializers.ValidationError("Comments are required when rejecting a space")
        return data