from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=20)
    sname = models.CharField(max_length=20)