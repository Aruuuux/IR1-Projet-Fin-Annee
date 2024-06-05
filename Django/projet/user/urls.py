# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name='login'),  # login view URL pattern
    path('login/', views.indexview, name='login'),
    path('index/', views.index, name='index'),
    path('psswrdforgot/', views.psswrdforgot, name='psswrdforgot'),
    path('admin/', views.admin, name='admin'),
    path('main/', views.main, name='main'),
    path('BDDviewer/', views.BDDviewer, main='BDDviewer')
]

from django.urls import path
from . import views

