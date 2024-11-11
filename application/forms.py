

from django import forms

from application.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your name'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your name'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your name'}),
        }