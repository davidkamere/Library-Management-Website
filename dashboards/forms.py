from django import forms
from .models import Borrowed


class BorrowForm(forms.ModelForm):

    class Meta:
        model = Borrowed
        fields = ('book',)
