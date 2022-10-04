from django.contrib import admin

from lessons.models import Person
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Person)
