# Evaluaciones Estudiantes

Sistema web desarrollado en Django para gestionar calificaciones de estudiantes con cálculo automático de promedios.

## Requisitos

- Python 3.10+
- pip

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/StevenInsuasti/LaboratorioFinal.git
cd LaboratorioFinal
```

### 2. Crear y activar el entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Accede en: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

## Estructura del proyecto

```
LaboratorioFinal/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── evaluaciones_estudiantes/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── calificaciones_estudiantes/
    ├── models.py          # Modelo Calificacion con cálculo de promedio
    ├── forms.py           # CalificacionForm y RegistroUsuarioForm
    ├── views.py           # Vistas de autenticación
    ├── urls.py            # Rutas de autenticación
    ├── migrations/
    └── templates/
        └── registration/
            ├── base.html
            ├── login.html
            └── registro.html
```

## Funcionalidades implementadas (Rol 1 - Steven)

- ✅ Proyecto Django configurado y corriendo
- ✅ Aplicación `calificaciones_estudiantes` registrada
- ✅ Modelo `Calificacion` con cálculo automático del promedio
- ✅ Migraciones aplicadas
- ✅ Sistema de registro de usuarios
- ✅ Sistema de login / logout
- ✅ Formulario `CalificacionForm` con validaciones (notas 0-5)
- ✅ Templates de autenticación con Bootstrap 5

## Equipo de desarrollo

| Rol | Integrante | Responsabilidad |
|-----|-----------|-----------------|
| 1 | Steven | Configuración inicial, autenticación, modelo |
| 2 | Sebastian | Vistas CRUD |
| 3 | Tatiana | Templates y presentación |
| 4 | Hector | Pruebas y promedio general |
