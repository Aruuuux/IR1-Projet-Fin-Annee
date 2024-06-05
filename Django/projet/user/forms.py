from django import forms
from databaseprojet.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'roles', 'date_of_birth',
            'speciality_id', 'photo', 'email', 'password', 'year'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False