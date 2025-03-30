# reporting/urls.py
from django.urls import path
from .views import (
    ReportGenerationAPIView,
    ReportTemplateListAPIView,
    GeneratedReportDetailAPIView
)

urlpatterns = [
    path('generate/', ReportGenerationAPIView.as_view(), name='generate-report'),
    path('templates/', ReportTemplateListAPIView.as_view(), name='report-templates'),
    path('reports/<int:pk>/', GeneratedReportDetailAPIView.as_view(), name='report-detail'),
]