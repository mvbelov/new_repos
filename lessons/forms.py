from django import forms
from django.core.exceptions import ValidationError

from .models import HomeWork, MyUser


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms. EmailField()
    phone = forms.CharField(max_length=50)


def fn(value):
    if value == 'Johan':
        return True
    raise ValidationError('Не Johan')


def Gora(value):
    if value == 'Жора':
        return True
    raise ValidationError('Не жора')


class PrForm(forms.Form):
    name = forms.CharField(validators=[fn, ])
    tel = forms.CharField(required=False, validators=[Gora])

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data, 'clean')


class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = '__all__'


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'