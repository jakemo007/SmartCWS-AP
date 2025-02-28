from rest_framework import viewsets, permissions
from .models import VerificationRequest
from .serializers import VerificationRequestSerializer

class VerificationRequestViewSet(viewsets.ModelViewSet):
    queryset = VerificationRequest.objects.all()
    serializer_class = VerificationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
