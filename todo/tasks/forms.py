from django import forms
from django.forms import ModelForm

from .models import * #all!

#To create a model form it's a class
class TaskForm(forms.ModelForm):
    class Meta: #receives two args: which model and what are the fields
        model = Task
        fields = '__all__'
    #now we import and render into the views.py!
