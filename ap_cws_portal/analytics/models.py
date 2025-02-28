from django.db import models
from django.conf import settings  # ✅ Ensures `CustomUser` is used

class BookingAnalytics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="booking_analytics")
    total_bookings = models.IntegerField(default=0)
    cancelled_bookings = models.IntegerField(default=0)
    successful_bookings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analytics for {self.user.username}"

class SpaceOccupancy(models.Model):
    space_provider = models.ForeignKey("spaces.SpaceProvider", on_delete=models.CASCADE, related_name="space_occupancy")
    total_seats = models.IntegerField()
    occupied_seats = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.space_provider.company_name} - Occupancy Data"
