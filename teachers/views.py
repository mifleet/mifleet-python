from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, TeacherDocumentation
from .serializers import TeacherDocumentationSerializer, TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDocumentationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teacher documentations to be viewed or edited.
    """
    queryset = TeacherDocumentation.objects.all()
    serializer_class = TeacherDocumentationSerializer