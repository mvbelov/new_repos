from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.PasswordInput()


class FormToValidate(forms.Form):
    login = forms.CharField(max_length=15, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    email = forms.CharField(max_length=255, required=False)

    def login_validator(self):
        if self.cleaned_data['login'] and self.cleaned_data['login'].isalpha():
            pass
        else:
            raise ValidationError

