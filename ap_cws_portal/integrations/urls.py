from django.urls import path
from .views import VerifyPlanAPIView

urlpatterns = [
    path('dpms/verify/', VerifyPlanAPIView.as_view(), name='dpms-verify'),
]