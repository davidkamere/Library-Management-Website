from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    id = forms.IntegerField()
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "id", "phone_number", "password1", "password2"]