# Generated by Django 5.0.6 on 2024-06-11 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseprojet', '0003_date_rename_course_id_absence_course_delete_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Speciality_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.speciality'),
        ),
    ]