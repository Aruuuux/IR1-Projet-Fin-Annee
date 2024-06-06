# user/urls.py
from django.urls import path
from . import views

from .views import test_email
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.indexview, name='login'),  # login view URL pattern
    path('login/', views.indexview, name='login'),
    path('createuser/', views.createuser, name='createuser'),
    path('edituser/<int:user_id>/', views.edituser, name='edituser'),
    path('deleteuser/<int:user_id>/', views.deleteuser, name='deleteuser'),
    path('psswrdforgot/', views.psswrdforgot, name='psswrdforgot'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('parametre/', views.parametre, name='parametre'),
    path('changepsswrd/',views.changepsswrd,name='changepsswrd'),
    path('test-email/', views.test_email,name='test_email'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

from django.urls import path
from . import views

