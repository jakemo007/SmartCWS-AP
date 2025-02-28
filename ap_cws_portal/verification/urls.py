from django.urls import path
from .views import SpaceVerificationListView

urlpatterns = [
    path('', SpaceVerificationListView.as_view(), name='space-verification-list'),
]
