from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#nn

class Roles(models.Model):
    ROLES = [
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Supervisor'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(choices=ROLES, unique=True)

    def __str__(self):
        return self.get_name_display()


class Speciality(models.Model):
    SPECIALITY_CHOICES = [
        (1, 'Informatique et réseaux'),
        (2, 'Automatique et systèmes embarqués'),
        (3, 'Génie Textile et Fibres'),
        (4, 'Génie Mécanique'),
        (5, 'Génie industriel'),
    ]
    id = models.AutoField(primary_key=True)
    speciality_id = models.IntegerField(choices=SPECIALITY_CHOICES, unique=True)
    name = models.CharField(max_length=255)
    responsible_id = models.IntegerField() 

    def __str__(self):
        return dict(self.SPECIALITY_CHOICES).get(self.speciality_id, 'Unknown')


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='../Media/photos/')
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=255)
    student_id = models.IntegerField(unique=True)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def clean(self):
        super().clean()
        email_pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@uha\.fr$'
        if not re.match(email_pattern, self.email):
            raise ValidationError(_('Email doit être sous la forme prenom.nom@uha.fr'))


    
class Module(models.Model):
    id=models.AutoField(primary_key=True)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    name= models.CharField(max_length=255)

class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    Number_of_credits=models.IntegerField() 
    Year=models.IntegerField() 
    Speciality_id=models.IntegerField() 
    coefficient=models.IntegerField() 
    module_id=models.ForeignKey(Module, on_delete=models.CASCADE)
    semester=models.IntegerField() 
    coefficient_lectures=models.IntegerField() 
    coefficient_PW=models.IntegerField() 
    coefficient_DW=models.IntegerField() 

class Score(models.Model):
    id=models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_score = models.FloatField()



class Course_type(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id=models.ForeignKey(User, on_delete=models.CASCADE)
    Score=models.FloatField()
    absence_number=models.IntegerField()
    course_type=models.IntegerField()



class Absence(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    date=models.DateField()
    student_id=models.ForeignKey(User, on_delete=models.CASCADE)