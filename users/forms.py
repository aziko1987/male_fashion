from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'your password'
    }), label=False)


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'your password'
    }), label=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'confirm password'
    }), label=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        user = UserModel.objects.all().filter(username=username).exists()
        if user:
            raise ValidationError(f'Ushbu {username} nomli username band !')
        return self.cleaned_data['username']

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar bir xil emas !')
        return self.cleaned_data['confirm_password']
