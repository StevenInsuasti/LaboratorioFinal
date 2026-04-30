"""
Configuración de URLs del proyecto evaluaciones_estudiantes.

Incluye las rutas de autenticación y delega las rutas del CRUD
a la aplicación calificaciones_estudiantes.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de autenticación
    path('', include('calificaciones_estudiantes.urls')),
    # Redirección raíz al login
    path('', lambda request: redirect('login'), name='home'),
]
