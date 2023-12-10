from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.TeacherViewSet)
router.register(r'documentation', views.TeacherDocumentationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
