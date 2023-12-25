from django.db import models

# Create your models here.

class Employee(models.Model):
      # class Employee(models.Model):
      # id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=100)
      email = models.EmailField()
      password = models.IntegerField(max_length=10)
      phone = models.IntegerField(max_length=10)