from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.DateField(auto_now=True)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.description