from django.db import models


from django.db import models

# Statut
class Status(models.Model):
    STATUS_CHOICES = [
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Supervisor'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(choices=STATUS_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Speciality(models.Model):
    SPECIALITY_CHOICES = [
        (1, 'Informatique et réseaux'),
        (2, 'Automatique et systèmes embarqués'),
        (3, 'Textile'),
        (4, 'Mécanique'),
        (5, 'Génie industriel'),
    ]
    id = models.AutoField(primary_key=True)
    speciality_id = models.IntegerField(choices=SPECIALITY_CHOICES, unique=True)
    name = models.CharField(max_length=255)
    responsible_id = models.IntegerField() 

    def __str__(self):
        return dict(self.SPECIALITY_CHOICES).get(self.speciality_id, 'Unknown')

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name