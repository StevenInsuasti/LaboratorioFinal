# 🧪 Guía de Pruebas Locales - Feature-3

## 📋 Prerequisitos

Antes de probar, asegúrate de tener:
- ✅ Python instalado
- ✅ Django instalado
- ✅ Base de datos configurada
- ✅ Migraciones aplicadas

---

## 🚀 Pasos para Probar Localmente

### 1. Preparar el Entorno

```bash
# Asegúrate de estar en la rama feature-3
git status

# Si no estás en feature-3, cámbiate
git checkout feature-3

# Verifica que tienes todos los cambios
git log --oneline -6
```

### 2. Aplicar Migraciones (si es necesario)

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Iniciar el Servidor

```bash
python manage.py runserver
```

El servidor debería iniciar en: `http://127.0.0.1:8000/`

---

## ✅ Checklist de Pruebas

### A. Autenticación

#### 1. Registro de Usuario
- [ ] Ir a: `http://127.0.0.1:8000/registro/`
- [ ] Verificar que el formulario se ve bien
- [ ] Llenar todos los campos:
  - Usuario: `tatiana_test`
  - Email: `tatiana@test.com`
  - Contraseña: `Test123456!`
  - Confirmar contraseña: `Test123456!`
- [ ] Click en "Crear Mi Cuenta"
- [ ] Verificar mensaje de éxito
- [ ] Verificar redirección a lista de calificaciones

#### 2. Cerrar Sesión
- [ ] Click en el menú de usuario (navbar)
- [ ] Click en "Cerrar Sesión"
- [ ] Verificar mensaje de confirmación
- [ ] Verificar redirección a login

#### 3. Iniciar Sesión
- [ ] Ir a: `http://127.0.0.1:8000/login/`
- [ ] Ingresar credenciales:
  - Usuario: `tatiana_test`
  - Contraseña: `Test123456!`
- [ ] Click en "Ingresar al Sistema"
- [ ] Verificar mensaje de bienvenida
- [ ] Verificar redirección a lista de calificaciones

---

### B. CRUD de Calificaciones

#### 1. Crear Calificación
- [ ] Click en "Nueva Calificación" (botón verde)
- [ ] O ir a: `http://127.0.0.1:8000/crear/`
- [ ] Verificar que el formulario se ve profesional
- [ ] Llenar el formulario:
  - Nombre: `Juan Pérez`
  - Identificación: `1234567890`
  - Asignatura: `Matemáticas`
  - Nota 1: `4.5`
  - Nota 2: `4.0`
  - Nota 3: `4.8`
- [ ] Click en "Guardar Calificación"
- [ ] Verificar mensaje de éxito
- [ ] Verificar que aparece en la lista
- [ ] Verificar que el promedio se calculó correctamente (4.43)

#### 2. Crear Más Calificaciones (para probar la tabla)
Crear al menos 3 calificaciones más con diferentes promedios:

**Calificación 2:**
- Nombre: `María García`
- ID: `0987654321`
- Asignatura: `Física`
- Notas: `3.0`, `3.5`, `3.2` (Promedio: 3.23 - amarillo)

**Calificación 3:**
- Nombre: `Pedro López`
- ID: `1122334455`
- Asignatura: `Química`
- Notas: `2.5`, `2.8`, `2.3` (Promedio: 2.53 - rojo)

**Calificación 4:**
- Nombre: `Ana Martínez`
- ID: `5544332211`
- Asignatura: `Inglés`
- Notas: `5.0`, `4.8`, `4.9` (Promedio: 4.90 - verde)

#### 3. Listar Calificaciones
- [ ] Ir a: `http://127.0.0.1:8000/listar/`
- [ ] Verificar que se muestran todas las calificaciones
- [ ] Verificar que la tabla es responsiva
- [ ] Verificar que los badges de promedio tienen colores correctos:
  - Verde: ≥ 3.5
  - Amarillo: ≥ 3.0 y < 3.5
  - Rojo: < 3.0
- [ ] Verificar que las estadísticas rápidas muestran el total
- [ ] Verificar que existe la sección de "Promedio General" (para Hector)
- [ ] Hacer hover sobre las filas (deben tener efecto)

#### 4. Editar Calificación
- [ ] Click en "Editar" (botón amarillo) de cualquier calificación
- [ ] Verificar que el formulario está pre-cargado
- [ ] Verificar que se muestra el promedio actual
- [ ] Cambiar alguna nota (por ejemplo, cambiar Nota 1 a `4.0`)
- [ ] Observar que el promedio se actualiza en tiempo real
- [ ] Click en "Actualizar Calificación"
- [ ] Verificar mensaje de éxito
- [ ] Verificar que los cambios se reflejan en la lista
- [ ] Verificar que el promedio se recalculó

#### 5. Eliminar Calificación
- [ ] Click en "Eliminar" (botón rojo) de cualquier calificación
- [ ] Verificar que se muestra la página de confirmación
- [ ] Verificar que se muestran todos los detalles del registro
- [ ] Verificar las advertencias (warning box y danger box)
- [ ] Click en "Cancelar" primero (debe volver a la lista)
- [ ] Volver a eliminar la misma calificación
- [ ] Click en "Sí, Eliminar Definitivamente"
- [ ] Verificar el alert de JavaScript (confirmación adicional)
- [ ] Aceptar el alert
- [ ] Verificar mensaje de éxito
- [ ] Verificar que la calificación ya no aparece en la lista

---

### C. Responsividad

#### 1. Vista Desktop (> 768px)
- [ ] Abrir en navegador normal
- [ ] Verificar que el navbar se ve completo
- [ ] Verificar que la tabla se ve bien
- [ ] Verificar que los formularios están centrados

#### 2. Vista Tablet (768px)
- [ ] Abrir DevTools (F12)
- [ ] Cambiar a vista responsive
- [ ] Configurar ancho: 768px
- [ ] Verificar que todo se adapta bien

#### 3. Vista Mobile (< 576px)
- [ ] Configurar ancho: 375px (iPhone)
- [ ] Verificar que el navbar muestra el menú hamburguesa
- [ ] Click en el menú hamburguesa
- [ ] Verificar que el menú se despliega
- [ ] Verificar que la tabla es scrolleable horizontalmente
- [ ] Verificar que los botones se apilan verticalmente
- [ ] Verificar que los formularios se adaptan

---

### D. Sistema de Mensajes

#### 1. Mensajes de Éxito (verde)
- [ ] Crear una calificación
- [ ] Verificar icono de check
- [ ] Verificar color verde
- [ ] Verificar que se puede cerrar (X)

#### 2. Mensajes de Error (rojo)
- [ ] Intentar crear calificación con ID duplicado
- [ ] Verificar icono de advertencia
- [ ] Verificar color rojo

#### 3. Mensajes de Info (azul)
- [ ] Cerrar sesión
- [ ] Verificar mensaje informativo

---

### E. Validaciones

#### 1. Validación HTML5
- [ ] Intentar enviar formulario vacío
- [ ] Verificar que el navegador muestra errores
- [ ] Intentar ingresar nota mayor a 5
- [ ] Verificar que no permite
- [ ] Intentar ingresar nota negativa
- [ ] Verificar que no permite

#### 2. Validación Django
- [ ] Intentar crear calificación con ID duplicado
- [ ] Verificar mensaje de error de Django
- [ ] Intentar ingresar nota fuera de rango (si pasa HTML5)
- [ ] Verificar mensaje de error

---

### F. Navegación

#### 1. Links del Navbar
- [ ] Click en "Sistema de Calificaciones" (logo)
- [ ] Debe ir a lista de calificaciones
- [ ] Click en "Calificaciones"
- [ ] Debe ir a lista de calificaciones
- [ ] Click en "Nueva Calificación"
- [ ] Debe ir a formulario de crear

#### 2. Botones de Acción
- [ ] Todos los botones "Cancelar" deben volver a la lista
- [ ] Todos los botones de guardar/actualizar deben funcionar
- [ ] Los botones de editar/eliminar deben ir a las páginas correctas

---

## 🎨 Aspectos Visuales a Verificar

### Colores
- [ ] Navbar: Gradiente azul
- [ ] Botón crear: Verde
- [ ] Botón editar: Amarillo
- [ ] Botón eliminar: Rojo
- [ ] Botón cancelar: Gris
- [ ] Badges de promedio: Verde/Amarillo/Rojo según valor

### Animaciones
- [ ] Hover en botones (elevación)
- [ ] Hover en filas de tabla
- [ ] Transiciones suaves
- [ ] Animación de entrada en eliminar.html

### Iconos
- [ ] Todos los iconos se muestran correctamente
- [ ] Iconos en navbar
- [ ] Iconos en formularios
- [ ] Iconos en botones
- [ ] Iconos en mensajes

### Tipografía
- [ ] Texto legible
- [ ] Jerarquía clara (h1, h2, etc.)
- [ ] Pesos de fuente apropiados

---

## 🐛 Problemas Comunes y Soluciones

### Problema: "Template does not exist"
**Solución:**
```python
# Verificar en settings.py que la app está registrada
INSTALLED_APPS = [
    ...
    'calificaciones_estudiantes',
]

# Verificar que TEMPLATES tiene la configuración correcta
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # Debe ser True
        ...
    },
]
```

### Problema: "Static files not loading"
**Solución:**
```bash
python manage.py collectstatic
```

### Problema: "Page not found (404)"
**Solución:**
Verificar que las URLs están configuradas en `evaluaciones_estudiantes/urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calificaciones_estudiantes.urls')),
]
```

### Problema: "CSRF verification failed"
**Solución:**
Verificar que todos los formularios tienen `{% csrf_token %}`

---

## 📸 Tomar Capturas de Pantalla

Mientras pruebas, toma capturas de:

1. **Login page** (desktop)
2. **Registro page** (desktop)
3. **Lista vacía** (sin calificaciones)
4. **Lista con datos** (tabla completa)
5. **Formulario crear** (desktop)
6. **Formulario editar** (desktop)
7. **Página eliminar** (confirmación)
8. **Mensajes de éxito/error**
9. **Vista móvil** (navbar hamburguesa)
10. **Vista móvil** (tabla responsive)

---

## ✅ Checklist Final de Pruebas

- [ ] Registro funciona
- [ ] Login funciona
- [ ] Logout funciona
- [ ] Crear calificación funciona
- [ ] Listar calificaciones funciona
- [ ] Editar calificación funciona
- [ ] Eliminar calificación funciona
- [ ] Validaciones funcionan
- [ ] Mensajes se muestran correctamente
- [ ] Diseño es responsivo
- [ ] Todos los iconos se muestran
- [ ] Animaciones funcionan
- [ ] No hay errores en consola del navegador
- [ ] No hay errores en consola de Django

---

## 🎉 ¡Pruebas Completadas!

Si todas las pruebas pasaron, estás listo para:
1. Tomar las capturas de pantalla
2. Crear el Pull Request
3. Notificar al equipo

**¡Excelente trabajo, Tatiana!** 🚀
