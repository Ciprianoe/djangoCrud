from .models import Task
from django import forms



class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','important']
        widgets = {
                'title':forms.TextInput(attrs={'class':'form-control','placeholder':'write a title'}),
                'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
                'important':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }