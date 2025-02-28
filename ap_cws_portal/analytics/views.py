from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, Count
from .models import BookingAnalytics, SpaceOccupancy
from .serializers import BookingAnalyticsSerializer, SpaceOccupancySerializer
from spaces.models import Booking, SpaceDetails

# ✅ Booking Analytics API
class BookingAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = BookingAnalytics.objects.all()
    serializer_class = BookingAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ Space Occupancy API
class SpaceOccupancyViewSet(viewsets.ModelViewSet):
    queryset = SpaceOccupancy.objects.all()
    serializer_class = SpaceOccupancySerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ Government Dashboard API (Aggregated Data)
class GovernmentDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_spaces = SpaceDetails.objects.count()
        total_seats = SpaceDetails.objects.aggregate(Sum("available_seats"))["available_seats__sum"] or 0
        occupied_seats = Booking.objects.filter(status="Confirmed").count()

        return Response({
            "total_spaces": total_spaces,
            "total_seats": total_seats,
            "occupied_seats": occupied_seats,
        })
