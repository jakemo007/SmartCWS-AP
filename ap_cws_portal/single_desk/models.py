# single_desk/models.py
from django.db import models
from django.utils import timezone

class BusinessRegistration(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=100)
    registration_date = models.DateField()
    status = models.CharField(max_length=50)
    last_verified = models.DateTimeField(default=timezone.now)
    raw_data = models.JSONField()

    class Meta:
        indexes = [
            models.Index(fields=['registration_number']),
            models.Index(fields=['business_name']),
        ]

    def __str__(self):
        return f"{self.business_name} ({self.registration_number})"