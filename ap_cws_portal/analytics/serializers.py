from rest_framework import serializers
from .models import BookingAnalytics, SpaceOccupancy

# ✅ Booking Analytics Serializer
class BookingAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAnalytics
        fields = "__all__"
        read_only_fields = ["created_at"]

# ✅ Space Occupancy Serializer
class SpaceOccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceOccupancy
        fields = "__all__"
        read_only_fields = ["updated_at"]
