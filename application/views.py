from django.shortcuts import render

from application.forms import StudentForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    form = StudentForm()
    return render(request, 'contact.html', {'forms': form})
