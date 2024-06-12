# user/urls.py
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('', views.indexview, name='login'),  # login view URL pattern
    path('login/', views.indexview, name='login'),
    path('createuser/', views.createuser, name='createuser'),
    path('edituser/<int:user_id>/', views.edituser, name='edituser'),
    path('deleteuser/<int:user_id>/', views.deleteuser, name='deleteuser'),
    path('psswrdforgot/', views.psswrdforgot, name='psswrdforgot'),
    path('userslist/', views.userslist, name='userslist'),
    path('importusers/', views.importusers, name='importusers'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('parametre/', views.parametre, name='parametre'),
    path('changepsswrd/',views.changepsswrd,name='changepsswrd'),
    path('edt/',views.edt,name='edt'),
    #path('emailsent/', views.emailsent, name='emailsent'),
    #path('test-email/', views.test_email, name='test_email'),
    #path('psswrdreset/<uidb64>/<token>/', views.psswrdreset, name='psswrdreset'),
   
    path('changepsswrd/', views.changepsswrd, name='changepsswrd'),
    path('404/', views.E404, name='E404'),
    path('500/', views.E500, name='E500'),
    path('403/', views.E403, name='E403'),
    path('400/', views.E400, name='E400'),

    path('password_reset/', views.psswrdforgot, name='password_reset'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Other URL patterns
    #nop
    

    

    ]

