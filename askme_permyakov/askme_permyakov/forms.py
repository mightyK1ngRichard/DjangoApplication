# Copyright © 2023 mightyK1ngRichard <dimapermyakov55@gmail.com>
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from askme.models import Author


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(min_length=4, widget=forms.PasswordInput, label='Пароль')

    def clean_password(self):
        # Пример проверки пароля.
        data = self.cleaned_data['password']
        if data == 'dmitriy is not boss':
            raise ValidationError('Wrong password')
        return data


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Старый пароль'
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Новый пароль'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Подтверждение нового пароля'
    )
