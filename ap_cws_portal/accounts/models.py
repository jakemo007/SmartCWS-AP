from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('ADMIN', 'Admin'),
        ('PROVIDER', 'Space Provider'),
        ('IT_FIRM', 'IT Firm'),
        ('ULB_OFFICER', 'Urban Local Body Officer'),
        ('DEVELOPER', 'CWS Developer'),
    ]

    role = models.CharField(max_length=20, choices=USER_ROLES, default='IT_FIRM')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    # Fix reverse accessor clashes by adding `related_name`
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
