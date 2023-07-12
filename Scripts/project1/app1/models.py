from django.db import models

# Create your models here.

class Student(models.Model):
    Email=models.CharField(max_length=90)
    Name=models.CharField(max_length=80)

