from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
from .models import Led1



class Led1Form(forms.ModelForm):
    class Meta:
        model = Led1
        fields = ['led1']
   