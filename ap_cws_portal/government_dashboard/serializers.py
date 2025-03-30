from rest_framework import serializers

class DistrictOccupancySerializer(serializers.Serializer):
    district = serializers.CharField()
    total_spaces = serializers.IntegerField()
    total_seats = serializers.IntegerField()
    occupied_seats = serializers.IntegerField()
    utilization_rate = serializers.FloatField()