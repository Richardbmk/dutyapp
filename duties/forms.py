from django import forms 
from django.forms import ModelForm 

from .models import *

class DutyForm(forms.ModelForm):

    class Meta:
        model = Duty
        fields = '__all__'