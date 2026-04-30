"""
Modelos de la aplicación calificaciones_estudiantes.

Define el modelo Calificacion con cálculo automático del promedio.
"""

from django.db import models


class Calificacion(models.Model):
    """
    Modelo que representa las calificaciones de un estudiante en una asignatura.

    El campo 'promedio' se calcula automáticamente al guardar el registro
    a partir de las tres notas ingresadas.
    """

    nombre_estudiante = models.CharField(
        max_length=150,
        verbose_name='Nombre del estudiante'
    )
    identificacion = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Identificación'
    )
    asignatura = models.CharField(
        max_length=100,
        verbose_name='Asignatura'
    )
    nota1 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Nota 1'
    )
    nota2 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Nota 2'
    )
    nota3 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Nota 3'
    )
    promedio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False,
        verbose_name='Promedio'
    )

    class Meta:
        verbose_name = 'Calificación'
        verbose_name_plural = 'Calificaciones'
        ordering = ['nombre_estudiante']

    def calcular_promedio(self):
        """Calcula el promedio de las tres notas redondeado a 2 decimales."""
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

    def save(self, *args, **kwargs):
        """Calcula el promedio automáticamente antes de guardar."""
        self.promedio = self.calcular_promedio()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.asignatura}"
