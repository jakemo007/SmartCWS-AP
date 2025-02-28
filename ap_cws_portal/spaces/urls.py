from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpaceProviderViewSet, ULBVerificationViewSet, SpaceDetailsViewSet, BookingViewSet, GovernmentDashboardViewSet

router = DefaultRouter()
router.register(r'space-providers', SpaceProviderViewSet, basename='space-provider')
router.register(r'ulb-verifications', ULBVerificationViewSet, basename='ulb-verification')
router.register(r'space-details', SpaceDetailsViewSet, basename='space-details')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path("", include(router.urls)),
    path("government-dashboard/", GovernmentDashboardViewSet.as_view(), name="government-dashboard"),
]
