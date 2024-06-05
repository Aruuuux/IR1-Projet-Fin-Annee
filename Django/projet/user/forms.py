from django import forms
from databaseprojet.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'roles', 'date_of_birth',
            'speciality_id', 'photo', 'password', 'year'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields.pop('email', None)
        self.fields['photo'].required = False
        self.fields['first_name'].initial = ''
        self.fields['last_name'].initial = ''