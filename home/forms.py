from django.forms import ModelForm
from django import forms
from django.forms import fields
from .models import *


class AddSubjectForm(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }

class AddClassForm(forms.ModelForm):
    
    class Meta:
        model = Standard
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            }

class AssignSubjectForm(forms.ModelForm):
    
    class Meta:
        model = AssignSubject
        fields = '__all__'
        widgets = {
            'classname' : forms.Select(attrs={'class':'form-select'}),
            'subjectname' : forms.CheckboxSelectMultiple(attrs={'class':'form-check-label'})
            }
    

class AddChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ['classname','subjectname','chname']
        widgets = {
            'classname' : forms.Select(attrs={'class':'form-select'}),
            'subjectname' : forms.Select(attrs={'class':'form-select'}),
            'chname' : forms.TextInput(attrs={'class':'form-control'}),
            }

        

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['subjectname'].queryset = Subject.objects.all()

        # if 'classname' in self.data:
        #     try:
        #         classid = int(self.data.get('classname'))
        #         self.fields['subjectname'].queryset = AssignSubject.objects.filter(classname=classid)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['subjectname'].queryset = self.instance.subject.city_set.order_by('name')



class UploadContent(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        widgets = {
            'classname' : forms.Select(attrs={'class':'form-select'}),
            'subjectname' : forms.Select(attrs={'class':'form-select'}),
            'chname' : forms.Select(attrs={'class':'form-select'}),
            'videourl' : forms.TextInput(attrs={'class':'form-control'}),
            'videotitle' : forms.TextInput(attrs={'class':'form-control'}),
            'assignmenturl' : forms.TextInput(attrs={'class':'form-control'}),
            'learningoutcome' : forms.TextInput(attrs={'class':'form-control'}),
            'added' : forms.DateInput(attrs={'type':'date'})
            }