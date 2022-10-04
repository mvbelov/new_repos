from django.urls import path

from lessons.views import get_car, get_fk_car, login_1, add_person, get_person, person_form, form_form, HomeworkCreate, login

app_name = 'lessons'
urlpatterns = [
    path('get_car/', get_car, name='get_car'),
    path('fk_get/', get_fk_car, name='get_fk_car'),
    path('login_1/', login_1, name='login_1'),
    path('add_person/', add_person, name='add_person'),
    path('person_list/', get_person, name='get_person'),
    path('person_form/', person_form, name='person_form'),
    path('form/', form_form, name='form_form'),
    # path('add_file/', home_home),
    path('homework/', HomeworkCreate.as_view()),
    path('login/', login, name='login'),
]
