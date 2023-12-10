from django.db import models

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE, related_name='user_teacher')
    vehicles = models.ManyToManyField('vehicles.Vehicle', related_name='teachers')

class TeacherDocumentation(models.Model):
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE, related_name='teacher')
    dni = models.FileField(upload_to='dni')
    circulation_permission = models.FileField(upload_to='circulation_permission')
    excersise_authorization = models.FileField(upload_to='excersise_authorization')
    distintive = models.FileField(upload_to='distintive')