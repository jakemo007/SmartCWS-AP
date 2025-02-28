from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CoworkingSpace(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    amenities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
