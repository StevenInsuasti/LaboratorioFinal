"""
URLs de la aplicación calificaciones_estudiantes.

Incluye rutas de autenticación y CRUD completo de calificaciones,
más la ruta para visualizar el promedio general.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # CRUD Calificaciones
    path('crear/', views.crear_calificacion, name='crear_calificacion'),
    path('listar/', views.listar_calificaciones, name='listar_calificaciones'),
    path('editar/<int:id>/', views.editar_calificacion, name='editar_calificacion'),
    path('eliminar/<int:id>/', views.eliminar_calificacion, name='eliminar_calificacion'),

    # Promedio general
    path('promedio-general/', views.promedio_general, name='promedio_general'),
]
