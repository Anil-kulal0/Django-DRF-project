# Generated by Django 4.1.5 on 2023-01-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100, verbose_name='Hospital Name')),
                ('hospital_contact', models.IntegerField(verbose_name='Contact Number')),
                ('hospital_address', models.TextField(verbose_name='Hospital Address')),
                ('hospital_emailid', models.EmailField(max_length=254)),
                ('hospital_specialization', models.CharField(max_length=200, verbose_name='Hospital Specialization')),
            ],
        ),
    ]
