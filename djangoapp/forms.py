from django import forms
from .models import *
from django.contrib.auth.models import User


class user_reg(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    cnfm=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','cnfm']
        
class userlogin(forms.Form):
    username=forms.CharField(max_length=50)
    password= forms.CharField(max_length=50)

class regform(forms.ModelForm):
    class Meta:
        model = regmodel
        fields='__all__' #['name','email','password']

class logform(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)



