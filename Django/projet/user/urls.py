# user/urls.py
from django.urls import path
from . import views


app_name = 'user'
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
    path('emailsent/', views.emailsent, name='emailsent'),
    #path('test-email/', views.test_email, name='test_email'),
    #path('psswrdreset/<uidb64>/<token>/', views.psswrdreset, name='psswrdreset'),
    path('password_change/', views.CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change_done/', views.CustomPasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/', views.CustomPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
     path('changepsswrd/', views.changepsswrd, name='changepsswrd'),
     path('404/', views.E404, name='E404'),
     path('500/', views.E500, name='E500'),
    path('403/', views.E403, name='E403'),
    path('400/', views.E400, name='E400'),
]



