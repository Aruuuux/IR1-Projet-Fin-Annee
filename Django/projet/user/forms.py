from django import forms
from databaseprojet.models import User,Roles,Speciality

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

class FilterForm(forms.Form):
    years = forms.MultipleChoiceField(
        choices=[
            ('1', '1ère année'),
            ('2', '2e année'),
            ('3', '3e année')
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    lessons = forms.ModelMultipleChoiceField(
        queryset=Roles.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    specialities = forms.ModelMultipleChoiceField(
        queryset=Speciality.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    student_id = forms.BooleanField(required=False)
    name = forms.BooleanField(required=False)