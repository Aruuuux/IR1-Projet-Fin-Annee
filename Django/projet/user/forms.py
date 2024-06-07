import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from databaseprojet.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "roles",
            "date_of_birth",
            "speciality_id",
            "photo",
            "password",
            "year",
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields.pop("email", None)
        self.fields["photo"].required = False
        self.fields["first_name"].initial = ""
        self.fields["last_name"].initial = ""

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_pattern = r"^[a-zA-Z]+\.[a-zA-Z]+@uha\.fr$"
        if not re.match(email_pattern, email):
            raise forms.ValidationError(
                "Email doit être sous la forme prenom.nom@uha.fr"
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
