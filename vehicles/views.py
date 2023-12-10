from django.shortcuts import render
from teachers.models import Teacher
from vehicles.models import Vehicle
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from vehicles.serializers import VehicleSerializer

# Create your views here.
class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all()

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        if(teacher): return teacher.vehicles.all()
        return self.queryset

