from django.contrib import admin

from vehicles.models import Vehicle, VehicleDocumentation

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(VehicleDocumentation)
