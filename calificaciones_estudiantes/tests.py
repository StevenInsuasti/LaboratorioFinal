"""
Tests unitarios para la aplicación calificaciones_estudiantes.

Cubre:
- Modelo Calificacion: cálculo automático de promedio
- Vistas CRUD: crear, listar, editar, eliminar
- Vista promedio general con función agregada Avg
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Calificacion


# ---------------------------------------------------------------------------
# Tests del Modelo
# ---------------------------------------------------------------------------

class CalificacionModelTest(TestCase):
    """Tests para el modelo Calificacion y su lógica de cálculo."""

    def setUp(self):
        self.calificacion = Calificacion.objects.create(
            nombre_estudiante="Juan Pérez",
            identificacion="1234567890",
            asignatura="Matemáticas",
            nota1=4.5,
            nota2=3.8,
            nota3=4.2,
        )

    def test_calculo_promedio(self):
        """El promedio debe calcularse correctamente al crear el registro."""
        promedio_esperado = round((4.5 + 3.8 + 4.2) / 3, 2)
        self.assertEqual(float(self.calificacion.promedio), promedio_esperado)

    def test_promedio_se_actualiza_al_guardar(self):
        """El promedio debe recalcularse cuando se modifican las notas."""
        self.calificacion.nota1 = 5.0
        self.calificacion.save()
        promedio_esperado = round((5.0 + 3.8 + 4.2) / 3, 2)
        self.assertEqual(float(self.calificacion.promedio), promedio_esperado)

    def test_str_representation(self):
        """El método __str__ debe retornar nombre y asignatura."""
        self.assertEqual(str(self.calificacion), "Juan Pérez - Matemáticas")

    def test_promedio_notas_perfectas(self):
        """Promedio de notas perfectas debe ser 5.0."""
        self.calificacion.nota1 = 5.0
        self.calificacion.nota2 = 5.0
        self.calificacion.nota3 = 5.0
        self.calificacion.save()
        self.assertEqual(float(self.calificacion.promedio), 5.0)

    def test_promedio_notas_minimas(self):
        """Promedio de notas cero debe ser 0.0."""
        self.calificacion.nota1 = 0.0
        self.calificacion.nota2 = 0.0
        self.calificacion.nota3 = 0.0
        self.calificacion.save()
        self.assertEqual(float(self.calificacion.promedio), 0.0)


# ---------------------------------------------------------------------------
# Tests de Vistas CRUD
# ---------------------------------------------------------------------------

class CalificacionCRUDTest(TestCase):
    """Tests de integración para las vistas CRUD de calificaciones."""

    def setUp(self):
        self.client = Client()
        # Crear usuario de prueba y autenticarlo
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )
        self.client.login(username='testuser', password='testpass123')

        # Registro base para tests de edición y eliminación
        self.calificacion = Calificacion.objects.create(
            nombre_estudiante="Ana García",
            identificacion="9876543210",
            asignatura="Física",
            nota1=4.0,
            nota2=3.5,
            nota3=4.5,
        )

    # --- Crear ---

    def test_crear_calificacion_get(self):
        """GET a crear debe retornar 200 y mostrar el formulario."""
        response = self.client.get(reverse('crear_calificacion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calificaciones/crear.html')

    def test_crear_calificacion_post_valido(self):
        """POST con datos válidos debe crear el registro y redirigir al listado."""
        datos = {
            'nombre_estudiante': 'Carlos López',
            'identificacion': '1111111111',
            'asignatura': 'Química',
            'nota1': '3.5',
            'nota2': '4.0',
            'nota3': '3.8',
        }
        response = self.client.post(reverse('crear_calificacion'), datos)
        self.assertRedirects(response, reverse('listar_calificaciones'))
        self.assertTrue(Calificacion.objects.filter(identificacion='1111111111').exists())

    def test_crear_calificacion_nota_mayor_cinco(self):
        """POST con nota > 5 debe fallar la validación y no crear el registro."""
        datos = {
            'nombre_estudiante': 'Pedro Ruiz',
            'identificacion': '2222222222',
            'asignatura': 'Historia',
            'nota1': '6.0',
            'nota2': '4.0',
            'nota3': '3.0',
        }
        response = self.client.post(reverse('crear_calificacion'), datos)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Calificacion.objects.filter(identificacion='2222222222').exists())

    def test_crear_calificacion_nota_negativa(self):
        """POST con nota negativa debe fallar la validación."""
        datos = {
            'nombre_estudiante': 'María Torres',
            'identificacion': '3333333333',
            'asignatura': 'Biología',
            'nota1': '-1.0',
            'nota2': '4.0',
            'nota3': '3.0',
        }
        response = self.client.post(reverse('crear_calificacion'), datos)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Calificacion.objects.filter(identificacion='3333333333').exists())

    # --- Listar ---

    def test_listar_calificaciones(self):
        """GET al listado debe retornar 200 y mostrar los registros."""
        response = self.client.get(reverse('listar_calificaciones'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calificaciones/listar.html')
        self.assertIn('calificaciones', response.context)

    def test_listar_incluye_promedio_general(self):
        """El contexto del listado debe incluir la clave promedio_general."""
        response = self.client.get(reverse('listar_calificaciones'))
        self.assertIn('promedio_general', response.context)

    # --- Editar ---

    def test_editar_calificacion_get(self):
        """GET a editar debe retornar 200 con el formulario pre-cargado."""
        response = self.client.get(
            reverse('editar_calificacion', args=[self.calificacion.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calificaciones/editar.html')

    def test_editar_calificacion_post_valido(self):
        """POST con datos válidos debe actualizar el registro."""
        datos = {
            'nombre_estudiante': 'Ana García Actualizada',
            'identificacion': '9876543210',
            'asignatura': 'Física Avanzada',
            'nota1': '5.0',
            'nota2': '4.5',
            'nota3': '4.8',
        }
        response = self.client.post(
            reverse('editar_calificacion', args=[self.calificacion.id]), datos
        )
        self.assertRedirects(response, reverse('listar_calificaciones'))
        self.calificacion.refresh_from_db()
        self.assertEqual(self.calificacion.nombre_estudiante, 'Ana García Actualizada')

    def test_editar_recalcula_promedio(self):
        """Al editar notas, el promedio debe recalcularse automáticamente."""
        datos = {
            'nombre_estudiante': 'Ana García',
            'identificacion': '9876543210',
            'asignatura': 'Física',
            'nota1': '5.0',
            'nota2': '5.0',
            'nota3': '5.0',
        }
        self.client.post(
            reverse('editar_calificacion', args=[self.calificacion.id]), datos
        )
        self.calificacion.refresh_from_db()
        self.assertEqual(float(self.calificacion.promedio), 5.0)

    # --- Eliminar ---

    def test_eliminar_calificacion_get(self):
        """GET a eliminar debe mostrar la página de confirmación."""
        response = self.client.get(
            reverse('eliminar_calificacion', args=[self.calificacion.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calificaciones/eliminar.html')

    def test_eliminar_calificacion_post(self):
        """POST a eliminar debe borrar el registro y redirigir al listado."""
        response = self.client.post(
            reverse('eliminar_calificacion', args=[self.calificacion.id])
        )
        self.assertRedirects(response, reverse('listar_calificaciones'))
        self.assertFalse(
            Calificacion.objects.filter(id=self.calificacion.id).exists()
        )


# ---------------------------------------------------------------------------
# Tests del Promedio General
# ---------------------------------------------------------------------------

class PromedioGeneralTest(TestCase):
    """Tests para la vista y cálculo del promedio general."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser2',
            password='testpass123',
        )
        self.client.login(username='testuser2', password='testpass123')

    def test_promedio_general_sin_registros(self):
        """Con la base de datos vacía, promedio_general debe ser None."""
        response = self.client.get(reverse('listar_calificaciones'))
        self.assertIsNone(response.context['promedio_general'])

    def test_promedio_general_con_registros(self):
        """El promedio general debe ser el promedio de todos los promedios individuales."""
        Calificacion.objects.create(
            nombre_estudiante="Est 1",
            identificacion="0000000001",
            asignatura="Mat",
            nota1=4.0,
            nota2=4.0,
            nota3=4.0,
        )
        Calificacion.objects.create(
            nombre_estudiante="Est 2",
            identificacion="0000000002",
            asignatura="Fis",
            nota1=2.0,
            nota2=2.0,
            nota3=2.0,
        )
        response = self.client.get(reverse('listar_calificaciones'))
        # Promedio de 4.0 y 2.0 = 3.0
        self.assertEqual(float(response.context['promedio_general']), 3.0)

    def test_vista_promedio_general_url(self):
        """La URL promedio-general/ debe responder con 200."""
        response = self.client.get(reverse('promedio_general'))
        self.assertEqual(response.status_code, 200)

    def test_promedio_general_url_sin_autenticacion(self):
        """Sin autenticación, la vista debe redirigir al login."""
        self.client.logout()
        response = self.client.get(reverse('promedio_general'))
        self.assertEqual(response.status_code, 302)


# ---------------------------------------------------------------------------
# Tests de Autenticación
# ---------------------------------------------------------------------------

class AutenticacionTest(TestCase):
    """Tests para las vistas de registro y login."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='usuarioexistente',
            password='clave12345',
        )

    def test_registro_get(self):
        """GET al registro debe retornar 200."""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)

    def test_registro_usuario_nuevo(self):
        """POST con datos válidos debe crear el usuario y redirigir."""
        datos = {
            'username': 'nuevousuario',
            'email': 'nuevo@test.com',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        }
        response = self.client.post(reverse('registro'), datos)
        self.assertRedirects(response, reverse('listar_calificaciones'))
        self.assertTrue(User.objects.filter(username='nuevousuario').exists())

    def test_login_exitoso(self):
        """Login con credenciales correctas debe redirigir al listado."""
        datos = {'username': 'usuarioexistente', 'password': 'clave12345'}
        response = self.client.post(reverse('login'), datos)
        self.assertRedirects(response, reverse('listar_calificaciones'))

    def test_login_fallido(self):
        """Login con credenciales incorrectas debe retornar 200 con error."""
        datos = {'username': 'usuarioexistente', 'password': 'claveincorrecta'}
        response = self.client.post(reverse('login'), datos)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Logout debe cerrar sesión y redirigir al login."""
        self.client.login(username='usuarioexistente', password='clave12345')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
