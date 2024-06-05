# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name='login'),  # login view URL pattern
    path('login/', views.indexview, name='login'),
    path('createuser/', views.createuser, name='createuser'),
    path('psswrdforgot/', views.psswrdforgot, name='psswrdforgot'),
]

from django.urls import path
from . import views

