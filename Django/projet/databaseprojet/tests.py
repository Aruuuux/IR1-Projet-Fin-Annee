from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

class UserModelTests(TestCase):
    
    def test_password_is_hashed(self):
        # Create a new user
        user = User.objects.create_user(
            email='testuser@uha.fr',
            password='Password123!',
            first_name='Test',
            last_name='User',
            roles='Student'
        )
        
        # Retrieve the user from the database
        db_user = User.objects.get(email='testuser@uha.fr')
        
        # Check that the password is hashed
        self.assertNotEqual(db_user.password, 'Password123!')
        self.assertTrue(check_password('Password123!', db_user.password))
