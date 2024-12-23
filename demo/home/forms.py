from django import forms
from .models import UserMaster

class UserMasterForm(forms.ModelForm):
    class Meta:
        model=UserMaster
        fields=['username','email','password','first_name','last_name']
        widgets={
            'password':forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=UserMaster
        fields=['username','password']
        widgets={
            'password':forms.PasswordInput(),
        }