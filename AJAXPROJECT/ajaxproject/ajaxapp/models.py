from django.db import models

# Create your models here.
class FileData(models.Model):
    title = models.CharField('Title', max_length=50)
    filename = models.FileField('Filename', upload_to='media/')
