# single_desk/urls.py
from django.urls import path
from .views import BusinessLookupAPIView, RegistrationSyncAPIView

urlpatterns = [
    path('lookup/', BusinessLookupAPIView.as_view(), name='business-lookup'),
    path('sync/', RegistrationSyncAPIView.as_view(), name='registration-sync'),
]