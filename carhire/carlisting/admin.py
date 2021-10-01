from django.contrib import admin
from .models import CarType, CarMake, CarModel, carInstance, Car, carOwner    

#Register the models here

admin.site.register(CarType)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(carInstance)
admin.site.register(Car)
admin.site.register(carOwner)