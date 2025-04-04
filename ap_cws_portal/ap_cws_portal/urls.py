from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Django Admin Panel
    path("api/accounts/", include("accounts.urls")),  # ✅ Authentication & User Management
    path("api/spaces/", include("spaces.urls")),  # ✅ Spaces & Bookings
    path("api/verification/", include("verification.urls")),  # ✅ Space Provider Verification
    path("api/analytics/", include("analytics.urls")),  # ✅ Seat Occupancy & Booking Reports
    path("api/notifications/", include("notifications.urls")),  # ✅ Notifications API
    path("api/api-auth/", include("rest_framework.urls")),  # ✅ API UI

    path('api/ulb/', include('ulb_verification.urls')),
    path('api/gov/', include('government_dashboard.urls')),
    path('api/dpms/', include('integrations.urls')),

    path('api/zonal/', include('apiic_integration.urls')),
    path('api/single-desk/', include('single_desk.urls')),
    path('api/reports/', include('reporting.urls')),
    path('api/compliance/', include('compliance.urls')),
]


# ✅ Serve media files (For document uploads like approval documents)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
