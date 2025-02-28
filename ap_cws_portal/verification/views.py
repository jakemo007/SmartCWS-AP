from rest_framework import generics
from .models import SpaceVerification
from .serializers import SpaceVerificationSerializer

class SpaceVerificationListView(generics.ListAPIView):
    queryset = SpaceVerification.objects.all()
    serializer_class = SpaceVerificationSerializer
