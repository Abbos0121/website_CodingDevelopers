from django import forms
from .models import AbstractUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AbstractUser
        fields = ['username', 'email', 'password']