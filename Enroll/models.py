from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=35)
    dob = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    mobile = models.CharField(max_length=10)
    pwd = models.CharField(max_length=15)
    cpwd = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=35)
    dob = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=15)