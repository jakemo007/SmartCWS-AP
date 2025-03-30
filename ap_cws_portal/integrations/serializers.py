from rest_framework import serializers

class PlanVerificationSerializer(serializers.Serializer):
    plan_number = serializers.CharField(
        max_length=50,
        required=True,
        help_text="DPMS plan approval number"
    )
    
    def validate_plan_number(self, value):
        if not value.startswith('AP'):
            raise serializers.ValidationError("Plan number must start with 'AP'")
        return value