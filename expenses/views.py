from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from teachers.models import Teacher
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    
    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        if teacher:
            return self.queryset.filter(teacher=teacher)
        return self.queryset

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        if teacher: return self.queryset.filter(teacher=teacher)
        return self.queryset