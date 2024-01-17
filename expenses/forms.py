# expenses/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            'required': 'This field is required.',
            'invalid': 'Please enter a valid username with letters, digits, and @/./+/-/_ only.',
            
        }
        
    )
    email = forms.EmailField(
        error_messages={
            'required': 'This field is required.',
            'invalid': 'Please enter a valid email address.',
        }
    )
    password1 = forms.CharField(
        error_messages={
            'required': 'This field is required.',
        },
        widget=forms.PasswordInput,
    )


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        error_messages={
            'required': 'This field is required.',
            'invalid': 'Please enter a valid username with letters, digits, and @/./+/-/_ only.'
        }
    )
    password = forms.CharField(
        error_messages={
            'required': 'This field is required.',
        },
        widget=forms.PasswordInput,
    )