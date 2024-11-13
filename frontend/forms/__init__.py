from django import forms

class CustomDateInput(forms.DateInput):
    input_type = 'date'

class CustomImageWidget(forms.ClearableFileInput):
    template_name = 'widgets/custom_image_widget.html'
