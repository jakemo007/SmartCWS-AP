# reporting/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ReportTemplate(models.Model):
    REPORT_TYPES = [
        ('occupancy', 'Space Occupancy'),
        ('financial', 'Financial Summary'),
        ('compliance', 'Compliance Status'),
    ]
    
    name = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    template_file = models.FileField(upload_to='report_templates/')
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parameters_schema = models.JSONField(default=dict)  # For dynamic form generation

    def __str__(self):
        return self.name

class GeneratedReport(models.Model):
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE)
    parameters = models.JSONField()  # Stores user inputs
    generated_file = models.FileField(upload_to='generated_reports/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']