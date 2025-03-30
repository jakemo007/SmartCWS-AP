from django.urls import path
from .views import ZonalApprovalListCreateView, ZonalApprovalDetailView

urlpatterns = [
    path('zonal-approvals/', ZonalApprovalListCreateView.as_view(), name='zonal-approval-list'),
    path('zonal-approvals/<int:verification_id>/', 
         ZonalApprovalDetailView.as_view(), 
         name='zonal-approval-detail'),
]