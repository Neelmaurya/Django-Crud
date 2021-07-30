from django.forms import ModelForm
from .models import Registration, Student
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'email', 'mobile', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }