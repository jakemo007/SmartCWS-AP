# compliance/urls.py
from django.urls import path
from .views import (
    GIGWRequirementListAPIView,
    GIGWRequirementDetailAPIView,
    ComplianceCheckAPIView,
    ComplianceReportAPIView
)

urlpatterns = [
    path('requirements/', GIGWRequirementListAPIView.as_view(), name='requirement-list'),
    path('requirements/<int:pk>/', GIGWRequirementDetailAPIView.as_view(), name='requirement-detail'),
    path('check/', ComplianceCheckAPIView.as_view(), name='compliance-check'),
    path('report/', ComplianceReportAPIView.as_view(), name='compliance-report'),
]