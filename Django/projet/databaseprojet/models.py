from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone 

class Roles(models.Model):
    ROLES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Supervisor', 'Supervisor'),
    ]
    name = models.CharField(max_length=50, choices=ROLES, unique=True)

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
    
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # Hachage du mdp
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('speciality_id'):
            speciality_id = extra_fields.pop('speciality_id')
            extra_fields['speciality_id'] = Speciality.objects.get(id=speciality_id)
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    roles = models.CharField(max_length=50, choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Supervisor', 'Supervisor')])
    date_of_birth = models.DateField(blank=True, null=True)
    speciality_id = models.ForeignKey('Speciality', on_delete=models.CASCADE, blank = True, null = True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=255)
    student_id = models.IntegerField(blank=True, null=True, unique=True)
    year = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True) # Statut de l'utilisateur
    is_staff = models.BooleanField(default=False) # Statut de l'utilisateur 
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    # Je ne sais pas vraiment à quoi servent ces 2 lignes mais il apparait qu'elles résolvent le problème du conflit django.contrib.auth (il y'avait un problème avec ces tables et je les ai créées manuellement sur dbbrowsersql)
    groups = models.ManyToManyField(Group, related_name='databaseprojet_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='databaseprojet_user_permissions_set', blank=True)

    objects = UserManager() # Pour assigner le gestionnaire personnalisé 'UseManager' à ce modèle
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'roles']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    def clean(self):
        '''
        super().clean()
        email_pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@uha\.fr$'
        if not re.match(email_pattern, self.email):
            raise ValidationError(_('Email doit être sous la forme prenom.nom@uha.fr'))
        '''
        if self.year is not None and not (self.year <= 3 or self.year == -1):
            raise ValidationError(_('Year must be less than 3 for students or equal to -1 for supervisors and teachers'))

class Module(models.Model):
    id=models.AutoField(primary_key=True)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    
    def clean(self):
        if self.year is not None and not (self.year <= 3 or self.year == -1):
            raise ValidationError(_('Year must be less than 3 for students or equal to -1 for supervisors and teachers'))

    

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Number_of_credits = models.IntegerField()
    Year = models.IntegerField()
    Speciality_id = models.IntegerField()
    coefficient = models.IntegerField()
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    semester = models.IntegerField()

    def __str__(self):
        return self.name


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
