# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # include user app URLs
    path('', RedirectView.as_view(url='/user/')),  # redirect root URL to login view
    path('accounts/', include('django.contrib.auth.urls')), 
    path('password_reset/done/', views.psswrdresetdone, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.psswrdresetcomplete, name='password_reset_complete'),
    path('module/', include('module.urls')),  # Include the module app's URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Pour gérer la localisation des photos ajoutées 