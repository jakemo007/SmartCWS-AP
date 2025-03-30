from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .dpms import DPMSService
from .serializers import PlanVerificationSerializer
from audit.decorators import log_api_action
from django.utils import timezone

class VerifyPlanAPIView(APIView):
    """
    API for DPMS plan verification with audit logging
    """
    permission_classes = [permissions.IsAuthenticated]

    @log_api_action
    def post(self, request):
        serializer = PlanVerificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        plan_number = serializer.validated_data['plan_number']
        try:
            is_valid = DPMSService.verify_plan(plan_number)
            return Response({
                "plan_number": plan_number,
                "is_valid": is_valid,
                "timestamp": timezone.now().isoformat()
            })
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )