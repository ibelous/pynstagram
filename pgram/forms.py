from django import forms
from .models import UserModel
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('profile_pic', )
