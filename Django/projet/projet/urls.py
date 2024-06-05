# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # include user app URLs
    path('', RedirectView.as_view(url='/user/')),  # redirect root URL to login view
]
