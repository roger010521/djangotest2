from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MaterialViewSet,
    ClientViewSet,
    ShoesViewSet,
    ProductionViewSet
)

router = DefaultRouter()
router.register(r'material', MaterialViewSet, basename='material')
router.register(r'client', ClientViewSet, basename='clients')
router.register(r'shoes', ShoesViewSet, basename='shoes')
router.register(r'production', ProductionViewSet, basename='production')

urlpatterns = [
    path('v1/', include(router.urls)),
]