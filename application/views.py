from django.shortcuts import redirect, render

from application.forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    data =  Student.objects.all()
    return render(request, 'about.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        
    else:
        form = StudentForm()    
    return render(request, 'contact.html', {'form': form})
