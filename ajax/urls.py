from django.urls import path

from ajax.views import get_json, get_page

app_name = 'ajax'

urlpatterns = [
    path('', get_json, name='get_json'),
    path('page1/', get_page, name='get_page'),
]
