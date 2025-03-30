from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .models import SpaceProvider,  SpaceDetails, Booking
from .serializers import SpaceProviderSerializer, ULBVerificationSerializer, SpaceDetailsSerializer, BookingSerializer
from ulb_verification.models import ULBVerification

# ✅ Space Provider API
class SpaceProviderViewSet(viewsets.ModelViewSet):
    queryset = SpaceProvider.objects.all()
    serializer_class = SpaceProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ✅ ULB Verification API
class ULBVerificationViewSet(viewsets.ModelViewSet):
    queryset = ULBVerification.objects.all()
    serializer_class = ULBVerificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(verified_by=self.request.user)

# ✅ Space Details API
class SpaceDetailsViewSet(viewsets.ModelViewSet):
    queryset = SpaceDetails.objects.all()
    serializer_class = SpaceDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ Booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ Government Dashboard API
class GovernmentDashboardViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_spaces = SpaceProvider.objects.count()
        total_seats = SpaceDetails.objects.aggregate(Sum("available_seats"))["available_seats__sum"]
        occupied_seats = Booking.objects.count()

        return Response({
            "total_spaces": total_spaces,
            "total_seats": total_seats,
            "occupied_seats": occupied_seats,
        })
