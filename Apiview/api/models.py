from django.db import models
from django.db.models import CharField,IntegerField
# Create your models here.
class Student(models.Model):
    name=CharField(max_length=100)
    roll=IntegerField()
    city=CharField(max_length=100)