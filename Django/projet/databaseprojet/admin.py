from django.contrib import admin
from .models import Roles, Speciality, User, Module, Course, Score, Course_type, Absence

admin.site.register(Roles)
admin.site.register(Speciality)
admin.site.register(User)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Score)
admin.site.register(Course_type)
admin.site.register(Absence)
