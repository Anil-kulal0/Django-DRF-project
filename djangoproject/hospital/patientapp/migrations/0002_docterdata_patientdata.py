# Generated by Django 4.1.5 on 2023-01-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docter_name', models.CharField(max_length=100, verbose_name='Docter Name')),
                ('docter_specilization', models.CharField(max_length=200, verbose_name='Specialization')),
                ('docter_doj', models.DateField(verbose_name='Date of Joining')),
            ],
        ),
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100, verbose_name='Patient Name')),
                ('patient_ward', models.CharField(max_length=10, verbose_name='Patient Ward')),
                ('patient_age', models.IntegerField(verbose_name='Patient Age')),
                ('patient_contact', models.IntegerField(verbose_name='Patient Contact')),
                ('patient_address', models.TextField(max_length=200, verbose_name='Patient Address')),
                ('patient_type', models.CharField(max_length=5, verbose_name='Patient Type')),
                ('patient_doa', models.DateField(verbose_name='Date of Addimission')),
                ('patient_dod', models.DateField(verbose_name='Date of Discharge')),
                ('patient_docter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.docterdata')),
                ('patient_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientapp.hospitaldata')),
            ],
        ),
    ]