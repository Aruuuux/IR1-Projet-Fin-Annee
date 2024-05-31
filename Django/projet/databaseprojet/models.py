from django.db import models


from django.db import models

# Statut
class Statut(models.Model):
    STATUT_CHOICES = [
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Supervisor'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.IntegerField(choices=STATUT_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name