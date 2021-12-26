
# forms.py
from django import forms
from .models import *
  
class imguploadform(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'image']