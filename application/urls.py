from django.contrib import admin
from django.urls import path


from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:student_id>/', views.delete_student, name='delete'),
    path('studentsapi/', views.studentsapi, name='studentsapi'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/edit/<int:id>/', views.edit_course, name='edit_course'),
    path('courses/add/', views.add_course, name='add_course'),
    path('students/<int:student_id>/assign_courses/', views.assign_course, name='assign_course'),
]