from rest_framework import serializers
from .models import SpaceProvider, ULBVerification, SpaceDetails, Booking

# ✅ Space Provider Serializer
class SpaceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceProvider
        fields = "__all__"
        read_only_fields = ["is_verified", "created_at"]

# ✅ ULB Verification Serializer
class ULBVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ULBVerification
        fields = "__all__"
        read_only_fields = ["verified_at"]

# ✅ Space Details Serializer
class SpaceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceDetails
        fields = "__all__"

# ✅ Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
