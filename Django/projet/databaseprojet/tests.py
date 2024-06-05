from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Roles, Speciality

class UserModelTests(TestCase):

    def setUp(self):
        self.role = Roles.objects.create(name='Student')
        self.speciality = Speciality.objects.create(speciality_id=1, name='Informatique et réseaux', responsible_id=1)

    def test_create_user_with_valid_email_successful(self):
        """Test creating a new user with a valid email is successful"""
        email = 'prenom.nom@uha.fr'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name='John',
            last_name='Doe',
            roles=self.role,
            date_of_birth='1990-01-01',
            speciality_id=self.speciality,
            student_id=12345,
            year=1
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'prenom.nom@UHA.FR'
        user = get_user_model().objects.create_user(email, 'test123', roles=self.role, date_of_birth='1990-01-01', speciality_id=self.speciality, student_id=12345, year=1)
        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123', roles=self.role, date_of_birth='1990-01-01', speciality_id=self.speciality, student_id=12345, year=1)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'super@uha.fr',
            'test123',
            first_name='Super',
            last_name='User',
            roles=self.role,
            date_of_birth='1990-01-01',
            speciality_id=self.speciality,
            student_id=0, 
            year=0
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
