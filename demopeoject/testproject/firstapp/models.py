from django.db import models

# Create your models here.
class userdata(models.Model):
    username = models.CharField("username", max_length=50)
    password = models.CharField("password",max_length=20)
