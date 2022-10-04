from django.contrib import admin

from lessons.models import Car, ShopCar, Concern, ModelSlag


admin.site.register(ShopCar)
admin.site.register(Concern)
admin.site.register(ModelSlag)
admin.site.register(Car)
