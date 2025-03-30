# reporting/serializers.py
from rest_framework import serializers
from .models import ReportTemplate, GeneratedReport

class ReportRequestSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
    parameters = serializers.JSONField()
    
    def validate_template_id(self, value):
        if not ReportTemplate.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Invalid template ID")
        return value

class ReportTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportTemplate
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at')

class GeneratedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedReport
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at')