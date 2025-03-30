# single_desk/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .client import SingleDeskClient
from .serializers import BusinessLookupSerializer

class BusinessLookupAPIView(APIView):
    """
    Endpoint to verify business registration with Single Desk Portal
    Example POST data: {"registration_number": "AP12345678"}
    """
    def post(self, request):
        serializer = BusinessLookupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = SingleDeskClient.get_business_details(
                serializer.validated_data['registration_number']
            )
            return Response({
                'status': 'verified',
                'data': data
            })
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

class RegistrationSyncAPIView(APIView):
    """
    Endpoint to sync all registered businesses (admin only)
    """
    def post(self, request):
        # Implement your sync logic here
        return Response({'status': 'sync initiated'})