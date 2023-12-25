from django.db import models

# Create your models here.

class Deparment(models.Model):
      name = models.CharField('Name',max_length=20, null=False)
      location = models.CharField('Location',max_length=50)
      def __str__(self):
            return self.name
class Role(models.Model):
      name = models.CharField('Name',max_length=50, null=False)
      def __str__(self):
            return self.name
      
      
class Employee(models.Model):
      first_name = models.CharField('First Name',max_length=20,null=False)
      last_name = models.CharField('Last Name',max_length=20)
      dept = models.ForeignKey(Deparment, on_delete= models.CASCADE)
      salary = models.IntegerField('Salary', default= 0)
      bouns = models.IntegerField('Bouns', default= 0)
      role = models.ForeignKey(Role, on_delete= models.CASCADE)
      phone = models.IntegerField('Phone Number', default= 0)
      hire_date = models.DateField()
      
      
      def __str__(self):
            return "%s %s " %(self.first_name, self.last_name)
      