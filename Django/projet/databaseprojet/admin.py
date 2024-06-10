from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Roles, Speciality, Module, Course, Score, Absence
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#Cette classe sert à la gestion des mdp entrés (il faut que les 2 soient identiques)
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'roles', 'date_of_birth', 'speciality_id', 'photo', 'student_id', 'year')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


#Cette classe sert comme configuration spécifique pour le modèle 'User' dans l'interface d'administration de Django
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'roles', 'date_of_birth', 'speciality_id', 'photo', 'student_id', 'year')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'roles', 'date_of_birth', 'speciality_id', 'photo', 'student_id', 'year', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
admin.site.register(Roles)
admin.site.register(Speciality)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Score)
admin.site.register(Absence)