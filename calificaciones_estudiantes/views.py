"""
Vistas de autenticación de la aplicación calificaciones_estudiantes.

Incluye registro, login y logout de usuarios.
Las vistas del CRUD serán implementadas por el equipo de desarrollo.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm


def registro_view(request):
    """
    Vista para el registro de nuevos usuarios.

    GET: Muestra el formulario de registro.
    POST: Procesa el formulario y crea el usuario si los datos son válidos.
    """
    if request.user.is_authenticated:
        return redirect('listar_calificaciones')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}! Tu cuenta fue creada exitosamente.')
            return redirect('listar_calificaciones')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registration/registro.html', {'form': form})


def login_view(request):
    """
    Vista para el inicio de sesión de usuarios.

    GET: Muestra el formulario de login.
    POST: Autentica al usuario y redirige si las credenciales son correctas.
    """
    if request.user.is_authenticated:
        return redirect('listar_calificaciones')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.username}!')
            return redirect('listar_calificaciones')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    """
    Vista para cerrar la sesión del usuario actual.

    Cierra la sesión y redirige al login.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
