from rest_framework import viewsets, permissions
from .models import CoworkingSpace
from .serializers import CoworkingSpaceSerializer

class CoworkingSpaceViewSet(viewsets.ModelViewSet):  # ✅ Allows GET, POST, PUT, DELETE
    queryset = CoworkingSpace.objects.all()
    serializer_class = CoworkingSpaceSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ Requires login for POST
