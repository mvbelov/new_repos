from django.urls import path

from jsonget.views import json_get, json_page

app_name = 'jsonget'

urlpatterns = [
    path('', json_get, name='json_get'),
    path('jsonpage1/', json_page, name='json_page'),
]
