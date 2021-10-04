from .models import *
from django import forms

class CSVForm(forms.ModelForm):
 class Meta:
  model = Csvs
  fields = ('filename',)
  labels = {'filename':'Upload CSV   '}

