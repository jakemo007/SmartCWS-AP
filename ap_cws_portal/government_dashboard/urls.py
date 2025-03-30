from django.urls import path
from .views import DistrictWiseOccupancyAPIView

urlpatterns = [
    path('district-occupancy/', 
         DistrictWiseOccupancyAPIView.as_view(), 
         name='district-occupancy'),
]