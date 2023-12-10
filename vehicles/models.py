from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    year = models.IntegerField()
    image = models.ImageField()
    plate_number = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return self.name

class VehicleDocumentation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_documentation')
    technical_sheet=models.FileField(upload_to='technical_sheet')
    circulation_document=models.FileField(upload_to='circulation_document')
    circulation_permission=models.FileField(upload_to='circulation_permission')
