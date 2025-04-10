# testproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', include('testapp.urls')),  # Change 'test/' back to 'htop/'
]