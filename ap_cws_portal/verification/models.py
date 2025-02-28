from django.db import models
from spaces.models import CoworkingSpace

class SpaceVerification(models.Model):
    space = models.OneToOneField(CoworkingSpace, on_delete=models.CASCADE)
    verified_by = models.CharField(max_length=255)
    verification_status = models.CharField(max_length=50, choices=[
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ])
    comments = models.TextField(blank=True, null=True)
    verified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Verification for {self.space.name}"
