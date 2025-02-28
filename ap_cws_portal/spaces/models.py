from django.db import models
from django.conf import settings  # ✅ Fix user reference issue

class SpaceProvider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="space_provider")  # ✅ Fix reference
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    floor_area = models.DecimalField(max_digits=10, decimal_places=2)
    facilities = models.TextField()
    approval_number = models.CharField(max_length=50, unique=True)
    approval_document = models.FileField(upload_to="approvals/")
    is_verified = models.BooleanField(default=False)  # ✅ Admin verification
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class ULBVerification(models.Model):
    space_provider = models.OneToOneField(SpaceProvider, on_delete=models.CASCADE, related_name="ulb_verification")
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="verified_spaces")  # ✅ Fix reference
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")])
    remarks = models.TextField(blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Verification for {self.space_provider.company_name} - {self.status}"

class SpaceDetails(models.Model):
    space_provider = models.ForeignKey(SpaceProvider, on_delete=models.CASCADE, related_name="space_details")
    available_seats = models.IntegerField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()

    def __str__(self):
        return f"{self.space_provider.company_name} - {self.available_seats} Seats"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_bookings")  # ✅ Fix reference
    space = models.ForeignKey(SpaceProvider, on_delete=models.CASCADE, related_name="space_bookings")  # ✅ Avoid clashes
    date = models.DateField()
    seat_count = models.IntegerField()
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Confirmed", "Confirmed"), ("Cancelled", "Cancelled")])

    def __str__(self):
        return f"Booking by {self.user.username} - {self.space.company_name}"
