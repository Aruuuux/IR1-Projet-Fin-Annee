from django import forms
from databaseprojet.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'roles', 'date_of_birth',
            'speciality_id', 'photo', 'email', 'password', 'student_id', 'year'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
