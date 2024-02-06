from dataclasses import field
from django import forms
from food.models import *
from django.contrib.auth.forms import *
from users.models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name']

class ProfileEditingForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'user_type']    