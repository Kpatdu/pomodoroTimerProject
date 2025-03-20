from django import forms
from .models import Timer

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['id', 'name', 'segment']
        # Apply CSS styles
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter segment',
                }),
        }