from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    id_number = forms.IntegerField()
    phone_number = forms.IntegerField()
    check_me_out = forms.BooleanField(required=True, label='I accept the Terms of Service')

    class Meta:
        model = User
        fields = ["first_name",
                  "last_name",
                  "email",
                  "id_number",
                  "phone_number",
                  "password1",
                  "password2",
                  "check_me_out"]
