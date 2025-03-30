from django.db import models
from django.contrib.auth import get_user_model
from ulb_verification.models import ULBVerification

User = get_user_model()

class ZonalApproval(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    ulb_verification = models.OneToOneField(
        ULBVerification,
        on_delete=models.CASCADE,
        related_name='zonal_approval'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    apiic_reference = models.CharField(max_length=50, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    inspection_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_approve_spaces", "Can approve spaces as Zonal Manager"),
        ]

    def __str__(self):
        return f"{self.ulb_verification.space.name} - {self.status}"