from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django_daraja.mpesa.core import MpesaClient

from application.forms import StudentForm
from application.models import Course, Student
from application.serializers import StudentSerializer
from school_project import student
from rest_framework import status
from rest_framework.decorators import api_view


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
        
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('about')  

@api_view(['GET', 'POST'])
def studentsapi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)  
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        name = request.POST['name']
        duration = request.POST['duration']
        description = request.POST['description']
        Course.objects.create(course_id=course_id, name=name, duration=duration, description=description)
        return redirect('course_list')
    return render(request, 'add_course.html')

def assign_course(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()

    if request.method == 'POST':
        selected_courses = request.POST.getlist('courses')  # Get selected course IDs
        student.courses.set(selected_courses)  # Assign courses to the student
        return redirect('students_list')

    return render(request, 'assign_course.html', {'student': student, 'courses': courses})
def edit_course(request, id):
    # Fetch the course object using the provided ID
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        # Update course details with the data from the form
        course.course_id = request.POST.get('course_id')
        course.name = request.POST.get('name')
        course.duration = request.POST.get('duration')
        course.description = request.POST.get('description')
        course.save()
        return redirect('course_list')  # After saving, redirect to course list

    return render(request, 'edit_course.html', {'course': course})
def delete_course(request, id):
    # Fetch the course object using the provided ID
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.delete()  # Delete the course
        return redirect('course_list')  # Redirect to the course list page after deletion

    return render(request, 'delete_course.html', {'course': course})

def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0791431287'
    amount = 1
    account_reference = 'eMobilis'
    transaction_desc = 'Payment for the web dev'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = client.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)
    