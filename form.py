from django.contrib.auth.models import User
from .models import Practical_test
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Practical_test
        fields = ['description','image']
