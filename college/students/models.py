from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    department= models.CharField(max_length=100)
    cgpa=models.FloatField()

    def __str__(self):
        return self.name

# Create your models here.
