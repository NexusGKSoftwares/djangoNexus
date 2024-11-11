from django.db import models

# Create your models here.
class   Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.CharField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=10) 
    

def __str__(self):
    return self.name