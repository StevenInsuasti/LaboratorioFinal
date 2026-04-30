"""
Vistas de la aplicación calificaciones_estudiantes.

Incluye autenticación (registro, login, logout) y CRUD completo
para la gestión de calificaciones de estudiantes.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, CalificacionForm
from .models import Calificacion


# ---------------------------------------------------------------------------
# Autenticación
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# CRUD Calificaciones
# ---------------------------------------------------------------------------

@login_required
def crear_calificacion(request):
    """
    Vista para registrar una nueva calificación.

    GET: Muestra el formulario vacío.
    POST: Valida y guarda la calificación; redirige al listado.
    """
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Calificación registrada exitosamente.')
                return redirect('listar_calificaciones')
            except Exception as e:
                messages.error(request, f'Error al guardar la calificación: {e}')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = CalificacionForm()

    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def listar_calificaciones(request):
    """
    Vista para mostrar todas las calificaciones registradas.

    Obtiene todos los registros ordenados según el Meta del modelo.
    """
    try:
        calificaciones = Calificacion.objects.all()
    except Exception as e:
        messages.error(request, f'Error al obtener las calificaciones: {e}')
        calificaciones = []

    return render(request, 'calificaciones/listar.html', {'calificaciones': calificaciones})


@login_required
def editar_calificacion(request, id):
    """
    Vista para actualizar una calificación existente.

    GET: Pre-carga el formulario con los datos actuales.
    POST: Valida y actualiza el registro; redirige al listado.
    """
    calificacion = get_object_or_404(Calificacion, id=id)

    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Calificación actualizada exitosamente.')
                return redirect('listar_calificaciones')
            except Exception as e:
                messages.error(request, f'Error al actualizar la calificación: {e}')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = CalificacionForm(instance=calificacion)

    return render(request, 'calificaciones/editar.html', {'form': form, 'calificacion': calificacion})


@login_required
def eliminar_calificacion(request, id):
    """
    Vista para eliminar una calificación.

    GET: Muestra pantalla de confirmación.
    POST: Elimina el registro y redirige al listado.
    """
    calificacion = get_object_or_404(Calificacion, id=id)

    if request.method == 'POST':
        try:
            calificacion.delete()
            messages.success(request, 'Calificación eliminada exitosamente.')
            return redirect('listar_calificaciones')
        except Exception as e:
            messages.error(request, f'Error al eliminar la calificación: {e}')

    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})
