
from django.db import models


# class Author(models.Model):
    
    
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=38)
    description = models.CharField(max_length= 255)
    added = models.DateTimeField(auto_now = True)
    # author = models.CharField(max_length=38, default="")
    # in_print = models.BooleanField(default=True)