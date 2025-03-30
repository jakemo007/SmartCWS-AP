from django.urls import path
from .views import SpaceVerificationList, VerifySpaceView

urlpatterns = [
    path('verifications/', SpaceVerificationList.as_view(), name='verification-list'),
    path('verify/<int:pk>/', VerifySpaceView.as_view(), name='verify-space'),
]