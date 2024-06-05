from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Roles, Speciality, Module, Course, Score, Course_type, Absence


# Cette classe sert comme configuration spécifique pour le modèle 'User' dans l'interface d'administration de Django

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
            'fields': ('email', 'first_name', 'last_name', 'roles', 'date_of_birth', 'speciality_id', 'photo', 'student_id', 'year', 'password1'),
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
admin.site.register(Course_type)
admin.site.register(Absence)
