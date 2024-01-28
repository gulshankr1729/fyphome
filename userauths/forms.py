from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'home__search-input', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'home__search-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'home__search-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'home__search-input', 'placeholder': 'Confirm Password'}))

    error_messages = {
        'password_mismatch': "The passwords do not match.",
        'unique_email': "An account with this email already exists.",
    }

    class Meta:
        model = User
        fields = ['username', 'email']
