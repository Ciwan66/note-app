from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder':'username'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'placeholder':'email'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder':'passowrd'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder':'password confirm'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    class Meta:
        model = User
        fields = ['username','password']