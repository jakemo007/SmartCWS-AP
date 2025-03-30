from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count, Sum, Q
from spaces.models import SpaceProvider as Space
from .serializers import DistrictOccupancySerializer
from datetime import timedelta
from django.utils import timezone

class DistrictWiseOccupancyAPIView(APIView):
    """
    Government dashboard endpoint for district-wise analytics
    """
    permission_classes = [permissions.IsAdminUser]  # Restrict to admin users

    def get(self, request):
        time_filter = request.query_params.get('timeframe', 'month')
        
        # Calculate time threshold based on filter
        if time_filter == 'week':
            threshold = timezone.now() - timedelta(days=7)
        elif time_filter == 'day':
            threshold = timezone.now() - timedelta(days=1)
        else:  # Default to monthly
            threshold = timezone.now() - timedelta(days=30)

        queryset = Space.objects.values('district').annotate(
            total_spaces=Count('id'),
            total_seats=Sum('capacity'),
            occupied_seats=Count(
                'bookings',
                filter=Q(
                    bookings__status='confirmed',
                    bookings__created_at__gte=threshold
                )
            ),
            utilization_rate=100.0 * Count(
                'bookings',
                filter=Q(bookings__status='confirmed')
            ) / Sum('capacity')
        ).order_by('district')

        serializer = DistrictOccupancySerializer(queryset, many=True)
        return Response({
            "timeframe": time_filter,
            "data": serializer.data,
            "last_updated": timezone.now().isoformat()
        })