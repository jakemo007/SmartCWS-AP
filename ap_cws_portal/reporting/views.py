# reporting/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Sum, Q
from datetime import timedelta
from django.utils import timezone
from .models import ReportTemplate, GeneratedReport
from .serializers import ReportRequestSerializer
from spaces.models import SpaceProvider as Space, Booking

class ReportGenerationAPIView(APIView):
    def post(self, request):
        serializer = ReportRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            template = ReportTemplate.objects.get(
                id=serializer.validated_data['template_id'],
                is_active=True
            )
            
            # Generate report based on type
            report_data = self._generate_report(
                template.report_type,
                serializer.validated_data['parameters']
            )
            
            # In production, you would save this to a file
            generated_report = GeneratedReport.objects.create(
                template=template,
                parameters=serializer.validated_data['parameters'],
                generated_file="",  # Add actual file path in production
                created_by=request.user
            )
            
            return Response({
                'status': 'success',
                'report_id': generated_report.id,
                'data': report_data
            })
            
        except ReportTemplate.DoesNotExist:
            return Response(
                {'error': 'Report template not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    def _generate_report(self, report_type, parameters):
        if report_type == 'occupancy':
            return self._generate_occupancy_report(parameters)
        elif report_type == 'financial':
            return self._generate_financial_report(parameters)
        elif report_type == 'compliance':
            return self._generate_compliance_report(parameters)
        
    def _generate_occupancy_report(self, params):
        timeframe = params.get('timeframe', 'month')
        date_threshold = timezone.now() - self._get_timedelta(timeframe)
        
        return Space.objects.annotate(
            occupied=Count('bookings', filter=Q(
                bookings__status='confirmed',
                bookings__created_at__gte=date_threshold
            )),
            utilization=100.0 * Count('bookings') / Sum('capacity')
        ).values('district', 'occupied', 'utilization')
    
    def _get_timedelta(self, timeframe):
        return {
            'day': timedelta(days=1),
            'week': timedelta(weeks=1),
            'month': timedelta(days=30),
            'year': timedelta(days=365)
        }.get(timeframe, timedelta(days=30))
    
# reporting/views.py (additional views)
from rest_framework import generics
from .serializers import ReportTemplateSerializer, GeneratedReportSerializer

class ReportTemplateListAPIView(generics.ListAPIView):
    queryset = ReportTemplate.objects.filter(is_active=True)
    serializer_class = ReportTemplateSerializer

class GeneratedReportDetailAPIView(generics.RetrieveAPIView):
    queryset = GeneratedReport.objects.all()
    serializer_class = GeneratedReportSerializer
    lookup_field = 'pk'