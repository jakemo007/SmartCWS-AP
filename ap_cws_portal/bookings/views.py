from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):  # ✅ Allow GET, POST, PUT, DELETE
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Requires login

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # ✅ Attach logged-in user
