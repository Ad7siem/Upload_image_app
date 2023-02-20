from django import forms
from django.forms import ModelForm
from .models import Images, Account


class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['image']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'