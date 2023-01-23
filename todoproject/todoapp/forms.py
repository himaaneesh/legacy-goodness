from .models import Task1
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Task1
        fields=['name','priority','date']
