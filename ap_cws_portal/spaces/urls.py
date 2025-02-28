from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoworkingSpaceViewSet

router = DefaultRouter()
router.register(r'spaces', CoworkingSpaceViewSet, basename='spaces')  # ✅ Correct registration

urlpatterns = [
    path('', include(router.urls)),  # ✅ Ensures all CRUD operations are registered
]
