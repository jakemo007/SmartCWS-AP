from django.db import models

class AnalyticsReport(models.Model):
    report_name = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    total_bookings = models.IntegerField()
    available_spaces = models.IntegerField()
    occupied_seats = models.IntegerField()

    def __str__(self):
        return self.report_name
