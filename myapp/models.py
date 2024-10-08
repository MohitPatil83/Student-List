from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    class_division = models.CharField(max_length=10)
    roll_number = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
   

    def _str_(self):
        return self.name