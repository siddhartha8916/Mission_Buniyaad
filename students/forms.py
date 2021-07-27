from django.core import validators
from django import forms
from django.forms import fields
from .models import Class, Chapter, Subject, Topic

class AddClass(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['classname']
        widgets = {
            'classname' : forms.TextInput(attrs={'class':'form-control'})
        }

class AddSubject(forms.ModelForm):
    class Meta:
        model=Subject
        fields = ['subname']
        widgets = {
            'subname' : forms.TextInput(attrs={'class':'form-control'})
        }



'''class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentUser
        fields = ['roll','admno','sname','fname','mname','gender','email','contact','password']
        widgets = {
            'roll' : forms.NumberInput(attrs={'class':'form-control'}),
            'admno' : forms.NumberInput(attrs={'class':'form-control'}),
            'sname' : forms.TextInput(attrs={'class':'form-control'}),
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'mname' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-select'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'contact' : forms.NumberInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }'''