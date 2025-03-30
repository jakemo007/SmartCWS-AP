from django.db.models import Q, Count
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import GIGWRequirement
from .serializers import GIGWRequirementSerializer

class GIGWRequirementListAPIView(generics.ListAPIView):
    queryset = GIGWRequirement.objects.all()
    serializer_class = GIGWRequirementSerializer

class GIGWRequirementDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = GIGWRequirement.objects.all()
    serializer_class = GIGWRequirementSerializer

class ComplianceCheckAPIView(APIView):
    def get(self, request):
        section = request.query_params.get('section')
        is_implemented = request.query_params.get('is_implemented')
        
        filters = Q()
        if section:
            filters &= Q(section__iexact=section)
        if is_implemented:
            filters &= Q(is_implemented=is_implemented.lower() == 'true')
        
        stats = GIGWRequirement.objects.filter(filters).aggregate(
            total=Count('id'),
            implemented=Count('id', filter=Q(is_implemented=True)),
            pending=Count('id', filter=Q(is_implemented=False))
        )
        
        stats['compliance_percentage'] = round(
            (stats['implemented'] / stats['total']) * 100, 2
        ) if stats['total'] > 0 else 0.0
        
        return Response(stats)

class ComplianceReportAPIView(APIView):
    def get(self, request):
        requirements = GIGWRequirement.objects.all()
        serializer = GIGWRequirementSerializer(requirements, many=True)
        
        return Response({
            'report_date': timezone.now().isoformat(),
            'requirements': serializer.data,
            'summary': {
                'total': requirements.count(),
                'implemented': requirements.filter(is_implemented=True).count(),
                'pending': requirements.filter(is_implemented=False).count()
            }
        })