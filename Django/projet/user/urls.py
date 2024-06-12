# user/urls.py
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
#from .views import export_users_to_excel

app_name = 'user'
urlpatterns = [
    path('', views.indexview, name='login'),  # login view URL pattern
    path('login/', views.indexview, name='login'),
    path('createuser/', views.createuser, name='createuser'),
    path('edituser/<int:user_id>/', views.edituser, name='edituser'),
    path('deleteuser/<int:user_id>/', views.deleteuser, name='deleteuser'),
    path('userslist/', views.userslist, name='userslist'),
    path('importusers/', views.importusers, name='importusers'),
    path('main/<int:user_id>/', views.main, name='main'),
    path('etudiant/<int:user_id>/', views.etudiant, name='etudiant'),
    path('supervisor/<int:user_id>/', views.supervisor, name='supervisor'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('parametre/', views.parametre, name='parametre'),
    path('changepsswrd/',views.changepsswrd, name='changepsswrd'),
    path('edt/', views.edt, name='edt'),
    path('error_400/', views.error_400, name='error_400'),
    path('error_403/', views.error_403, name='error_403'),
    path('error_404/', views.error_404, name='error_404'),
    path('error_500/', views.error_500, name='error_500'),
    path('password_reset/', views.passwordreset, name='password_reset'),
    
    ]

