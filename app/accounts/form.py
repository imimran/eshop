from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class UserRegistationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistationForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'first_name', 'last_name', 'phone', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model= User
        fields= ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')
   

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Email or Password')

     
