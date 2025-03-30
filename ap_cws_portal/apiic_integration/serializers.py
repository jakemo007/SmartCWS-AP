from rest_framework import serializers
from .models import ZonalApproval

class ZonalApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonalApproval
        fields = [
            'id', 'ulb_verification', 'status', 'apiic_reference',
            'approved_by', 'inspection_date', 'comments',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'approved_by']

    def validate(self, data):
        if data.get('status') == 'approved' and not data.get('apiic_reference'):
            raise serializers.ValidationError("APIIC reference is required for approval")
        return data