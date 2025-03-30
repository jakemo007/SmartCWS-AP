# ulb_verification/models.py
from django.conf import settings
from django.db import models
from spaces.models import SpaceProvider

class ULBVerification(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    space = models.OneToOneField(
        SpaceProvider,
        on_delete=models.CASCADE,
        related_name='ulb_verification'
    )
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True)
    verification_date = models.DateTimeField(auto_now_add=True)