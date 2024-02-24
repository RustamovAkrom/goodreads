from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        user.save()
      
    class Meta:
        model = User
        fields = ['username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password', 
                  'avatar', 
                  'middle_name']
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     "type":"text", "id":"name", "placeholder":"Username..."
    # }))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     "type":"text", "id":"first_name", "placeholder":"First name..."
    # }))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     "type":"text", "id":"last_name", "placeholder":"Last name..."
    # }))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     "type":"email", "id":"email", "placeholder":"Your email..."
    # }))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     "type":"text", "id":"password", "placeholder":"password..."
    # }))
    # avatar = forms.FileField(widget=forms.FileInput(attrs={
    #     "type":"file", "id":"avatar"
    # }))
    # middle_name = forms.FileField(widget=forms.FileInput(attrs={
    #     "type":"text", "id":"middle_name"
    # }))
        
    
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Enter sername"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"Enter password"}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password', 
                  'avatar', 
                  'middle_name']