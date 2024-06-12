# module/urls.py

from django.urls import path

from . import views
from .views import *

app_name = 'module'  # This sets the app namespace to 'module'

urlpatterns = [
    path('create/', views.create_module, name='create_module'),
    path('<int:module_id>/create_course/', views.create_course, name='create_course'),
    path('<int:module_id>/edit_module/', views.edit_module, name='edit_module'),
    path('<int:module_id>/delete/', views.delete_module, name='delete_module'),
    path('course/<int:course_id>/manage_course/', views.manage_course, name='manage_course'),
    path('editabsence/<int:pk>/', views.editabsence, name='editabsence'),
    path('deleteabsence/<int:absence_id>/', views.deleteabsence, name='deleteabsence'),
    path('editscore/<int:pk>/', views.editscore, name='editscore'),
    path('deletescore/<int:score_id>/', views.deletescore, name='deletescore'),
    path('editcourse/<int:course_id>/', views.editcourse, name='editcourse'),
    path('deletecourse/<int:course_id>/', views.deletecourse, name='deletecourse'),
]
