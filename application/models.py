# models.py
from django.db import models

class Student(models.Model):
    photo = models.ImageField(upload_to='photos/')
    adm = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True)  
    name = models.CharField(max_length=100)  
    duration = models.IntegerField(help_text="Duration in months")  
    description = models.TextField(blank=True)  

    def __str__(self):
        return f"{self.course_id} - {self.name}"