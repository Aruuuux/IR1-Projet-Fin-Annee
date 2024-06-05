# Generated by Django 5.0.6 on 2024-06-05 12:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('Number_of_credits', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('Speciality_id', models.IntegerField()),
                ('coefficient', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('coefficient_lectures', models.IntegerField()),
                ('coefficient_PW', models.IntegerField()),
                ('coefficient_DW', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Supervisor', 'Supervisor')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('speciality_id', models.IntegerField(choices=[(1, 'Informatique et réseaux'), (2, 'Automatique et systèmes embarqués'), (3, 'Génie Textile et Fibres'), (4, 'Génie Mécanique'), (5, 'Génie industriel')], unique=True)),
                ('name', models.CharField(max_length=255)),
                ('responsible_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='../Media/photos/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField(max_length=255)),
                ('student_id', models.IntegerField(unique=True)),
                ('year', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='databaseprojet_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='databaseprojet_user_permissions_set', to='auth.permission')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.roles')),
                ('speciality_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.speciality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Score', models.FloatField()),
                ('absence_number', models.IntegerField()),
                ('course_type', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.module'),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_score', models.FloatField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='speciality_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseprojet.speciality'),
        ),
    ]
