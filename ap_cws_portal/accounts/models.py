from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("provider", "Space Provider"),
        ("it_firm", "IT Firm"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="it_firm")
    is_verified = models.BooleanField(default=False)  # ✅ Admin verifies providers

    groups = models.ManyToManyField(
        Group, related_name="customuser_accounts_groups", blank=True  # ✅ Fix conflict
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_accounts_permissions", blank=True  # ✅ Fix conflict
    )

    def __str__(self):
        return self.username
