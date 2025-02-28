from django.urls import path
from .views import AnalyticsReportListView

urlpatterns = [
    path('reports/', AnalyticsReportListView.as_view(), name='analytics-reports'),
]
