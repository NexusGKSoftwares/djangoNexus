# forms.py
from django import forms
from application.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'adm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your admission number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your course'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'placeholder': 'Upload your image'})
        }
