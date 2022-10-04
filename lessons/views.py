from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from lessons.forms import PersonForm, PrForm, HomeWorkForm, MyUserForm
from lessons.models import Car, Concern, Person, HomeWork


def get_car(request):
    car = Car.objects.all()
    print(car.query)
    return render(request, 'cars.html')


def get_fk_car(request):
    car = Car.objects.select_related('concern')
    context = {'concern_for_id': car}
    return render(request, 'fk_car.html', context)

l='Alex'
p='12345'

def login_1(request):
    print(request.POST)
    if request.method == 'POST':
        if l == request.POST.get('login'):
            return HttpResponse('Вы вошли в кабинет')
        else:
            return HttpResponse('Неверный логин или пароль')
    return HttpResponse('Вы вошли в кабинет')


def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        person = Person.objects.create(name=name, surname=surname, email=email)
        context = {'succes': 'Успешно сохраниено'}
        return render(request, 'person.html', context)
    return render(request, 'person.html')


def get_person(request):
    person = Person.objects.filter(is_show=True)
    context = {'person': person}
    return render(request, 'person_list.html', context)


def person_form(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print(form.__dict__['data'])
    context = {'form': form}
    return render(request, 'person_form.html', context)


def form_form(request):
    form = PrForm()
    if request.method == 'POST':
        form = PrForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data, 'view')
            form.clean()
    context = {'form': form}
    return render(request, 'form_django.html', context)


# def home_home(request):
#     form = HomeWorkForm()
#     if request.method == "POST":
#         form = HomeWorkForm(request.POST, request.FILES)
#         if form.is_valid():
#             date = form.cleaned_data
#             HomeWork.objects.create(name=date['name'], photo=date['photo'], file=date['file'])
#     context = {'form': form}
#     return render(request, 'home.html', context)


class HomeworkCreate(CreateView):
    form_class = HomeWorkForm
    model = HomeWork
    template_name = 'home.html'
    success_url = 'http://127.0.0.1:8000/homework/'


def login(request):
    form = MyUserForm()
    print(request.COOKIES)
    print(request.COOKIES.get('name'))
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    context = {'form': form}
    responce = render(request, 'login.html', context=context)
    responce.set_cookie('color', request.COOKIES.get('color'))
    return responce
    # return render(request, 'login.html', context=context)