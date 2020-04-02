from django import forms
from .models import Borrowed, Waiting


class BorrowForm(forms.ModelForm):

    class Meta:
        model = Borrowed
        fields = ('book',)


class WaitingForm(forms.ModelForm):

    class Meta:
        model = Waiting
        fields = ('book',)