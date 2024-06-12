# user/urls.py
from django.urls import path, include
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
    path('email_sent/', views.email_sent, name='email_sent'),
    #path('test-email/', views.test_email, name='test_email'),
    #path('psswrdreset/<uidb64>/<token>/', views.psswrdreset, name='psswrdreset'),
    path('error_400/', views.error_400, name='error_400'),
    path('error_403/', views.error_403, name='error_403'),
    path('error_404/', views.error_404, name='error_404'),
    path('error_500/', views.error_500, name='error_500'),
    #path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    #path('password_reset/', views.password_resethtml, name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    #path('password_reset/done/', views.password_resetdonehtml, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_forgotten/', views.password_forgotten, name='password_forgotten'),
    #path('addgrade/', views.addgrade, name='addgrade'),
    path('logout/', views.logout_view, name='logout'),

    ]

