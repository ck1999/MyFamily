from django.contrib.auth.models import User
from django import forms
from .models import UserUI
from django.contrib.auth.forms import UserCreationForm

class UserUIAddForm(forms.ModelForm):
    fio = forms.CharField(max_length=40, required=True)
    needUser = forms.BooleanField()
    pos_x = forms.FloatField()
    pos_y = forms.FloatField()

    class Meta:
        model = UserUI
        fields = (
            'fio',
            'needUser'
        )