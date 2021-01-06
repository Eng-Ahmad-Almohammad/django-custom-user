from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CusomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'email','username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ( 'email','username')

