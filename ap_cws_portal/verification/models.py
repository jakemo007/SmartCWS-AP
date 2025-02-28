from django.db import models
from accounts.models import CustomUser

class VerificationRequest(models.Model):
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document = models.FileField(upload_to="verification/")
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")])
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Verification for {self.provider.username} - {self.status}"
