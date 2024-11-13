from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    admission = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return self.name
