# Copyright © 2023 mightyK1ngRichard <dimapermyakov55@gmail.com>
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)

    def clean_password(self):
        # Пример проверки пароля
        data = self.cleaned_data['password']
        if data == 'dmitriy is not boss':
            raise ValidationError('Wrong password')
        return data
