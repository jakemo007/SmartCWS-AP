from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingAnalyticsViewSet, SpaceOccupancyViewSet, GovernmentDashboardView

router = DefaultRouter()
router.register(r'booking-analytics', BookingAnalyticsViewSet, basename="booking-analytics")
router.register(r'space-occupancy', SpaceOccupancyViewSet, basename="space-occupancy")

urlpatterns = [
    path("", include(router.urls)),
    path("government-dashboard/", GovernmentDashboardView.as_view(), name="government-dashboard"),
]
