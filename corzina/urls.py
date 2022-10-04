from django.urls import path

from corzina.views import get_category, get_product

urlpatterns = [
    path('category/', get_category, name='get_category'),
    path('category/<str:slug>', get_product, name='get_product'),
]
