from django.urls import include, path
from django.urls import include, path
from rest_framework import routers
from .views import VehicleViewSet

router = routers.DefaultRouter()
router.register(r'', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
