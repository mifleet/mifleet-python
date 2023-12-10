from rest_framework import serializers
from .models import Teacher, TeacherDocumentation

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDocumentation
        fields = '__all__'
