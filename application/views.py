from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from application.forms import StudentForm
from application.models import Student
from school_project import student


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    data =  Student.objects.all()
    return render(request, 'about.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
        
    else:
        form = StudentForm()    
    return render(request, 'contact.html', {'form': form})

def edit(request,id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'student updated successfully')
            return redirect('about')
        else:
            messages.error(request, 'please check form details')
        
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form':form,'student':student})
        