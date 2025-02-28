from rest_framework import generics
from .models import AnalyticsReport
from .serializers import AnalyticsReportSerializer

class AnalyticsReportListView(generics.ListAPIView):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer
