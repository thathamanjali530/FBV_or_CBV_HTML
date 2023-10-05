from django.db import models

# Create your models here.

class student(models.Model):
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Email=models.EmailField()
