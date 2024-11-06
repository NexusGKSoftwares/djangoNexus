from django.shortcuts import render

def index(request):
    return render(request, 'application/index.html')

def about(request):
    return render(request, 'application/about.html')
def contact(request):
    return render(request, 'application/contact.html')
def base(request):
    return render(request, 'application/base.html')
