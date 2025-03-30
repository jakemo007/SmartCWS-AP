from rest_framework import generics, permissions
from .models import ZonalApproval
from .serializers import ZonalApprovalSerializer
from django.shortcuts import get_object_or_404

class ZonalApprovalListCreateView(generics.ListCreateAPIView):
    queryset = ZonalApproval.objects.all()
    serializer_class = ZonalApprovalSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(approved_by=self.request.user)

class ZonalApprovalDetailView(generics.RetrieveUpdateAPIView):
    queryset = ZonalApproval.objects.all()
    serializer_class = ZonalApprovalSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
    lookup_field = 'ulb_verification_id'
    lookup_url_kwarg = 'verification_id'