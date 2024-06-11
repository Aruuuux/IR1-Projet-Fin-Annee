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
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('parametre/', views.parametre, name='parametre'),
    path('edt/',views.edt,name='edt'),
    #path('emailsent/', views.emailsent, name='emailsent'),
    #path('test-email/', views.test_email, name='test_email'),
    #path('psswrdreset/<uidb64>/<token>/', views.psswrdreset, name='psswrdreset'),
    #path('export/excel/', export_users_to_excel, name='export_users_to_excel'),
    #path('export/csv/', export_users_to_csv, name='export_users_to_csv'),
    #path('changepsswrd/', views.changepsswrd, name='changepsswrd'),
    path('password_reset/', views.psswrdforgot, name='password_reset'),
    path('addgrade/', views.addgrade, name='addgrade'),
     path('error_400/', views.error_400, name='error_400'),
     path('error_403/', views.error_403, name='error_403'),
     path('error_404/', views.error_404, name='error_404'),
     path('error_500/', views.error_500, name='error_500'),
     path('changepsswrd/', views.changepsswrd,name='changepsswrd'),
     path('psswrdforgot/', views.psswrdforgot, name='psswrdforgot'),
     path('password_reset/', views.psswrdforgot, name='password_reset'),
    ]