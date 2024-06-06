# user/urls.py
from django.urls import path
from . import views

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
    path('changepsswrd/',views.changepsswrd,name='changepsswrd')
    path('404/', views.E404, name='page404'),
]

from django.urls import path
from . import views

