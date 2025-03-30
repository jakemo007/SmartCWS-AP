from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import ULBVerification
from .serializers import ULBVerificationSerializer
from spaces.models import SpaceProvider as Space
from django.shortcuts import get_object_or_404

class SpaceVerificationList(generics.ListAPIView):
    serializer_class = ULBVerificationSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = ULBVerification.objects.all()

    def get_queryset(self):
        return self.queryset.filter(status='pending')

class VerifySpaceView(generics.UpdateAPIView):
    serializer_class = ULBVerificationSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    queryset = ULBVerification.objects.all()

    def perform_update(self, serializer):
        serializer.save(verified_by=self.request.user)