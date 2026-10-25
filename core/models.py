from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    titulo_academico = models.CharField(max_length=150, verbose_name="Título académico")
    biografia = models.TextField(verbose_name="Biografía")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    dedicacion = models.CharField(max_length=150, verbose_name="Dedicación")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
