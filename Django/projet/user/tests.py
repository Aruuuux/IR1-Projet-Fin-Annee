from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UserForm
from databaseprojet.models import Roles, Speciality, User

class UserFormTests(TestCase):

    def setUp(self):
        self.role = Roles.objects.create(name='Student')
        self.speciality = Speciality.objects.create(speciality_id=1, name='Informatique et réseaux', responsible_id=1)

    def test_valid_email(self):
        """Test that the email validation allows valid emails"""
        form_data = {
            'first_name': 'hamza',
            'last_name': 'baya',
            'roles': self.role,
            'date_of_birth': '1990-01-01',
            'speciality_id': self.speciality.id,
            'email': 'hamza.baya@uha.fr',
            'password': 'testpass123',
            'student_id': 12345,
            'year': 1
        }
        form = UserForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # Imprimer les erreurs pour voir ce qui ne va pas
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Test that the email validation catches invalid emails"""
        form_data = {
            'first_name': 'hamza',
            'last_name': 'baya',
            'roles': self.role,
            'date_of_birth': '1990-01-01',
            'speciality_id': self.speciality.id,
            'email': 'hamza@uha.fr',
            'password': 'testpass123',
            'student_id': 12345,
            'year': 1
        }
        form = UserForm(data=form_data)
        if form.is_valid():
            print(form.cleaned_data)  # Imprimer les données nettoyées pour déboguer
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
