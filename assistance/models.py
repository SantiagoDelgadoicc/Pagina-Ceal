from django.db import models

class SolicitudAcademica(models.Model):
    RAMOS_CHOICES = [
        ('CALCULO', 'Cálculo I/II'),
        ('FISICA', 'Fisica I/II'),
        ('BD', 'Base de Datos'),
        ('PROG', 'Programación'),
    ]

    ramo = models.CharField(max_length=50, choices=RAMOS_CHOICES)
    cantidad_estudiantes = models.PositiveIntegerField(default=1)
    info_contacto = models.TextField()
    fecha_limite = models.DateField()
    is_approved = models.BooleanField(default=False) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        estado = "Aprobada" if self.is_approved else "Pendiente"
        return f"Solicitud {self.get_ramo_display()} - {estado}"

class Ayudantia(models.Model):
    ramo = models.CharField(max_length=100)
    ayudante = models.CharField(max_length=100)
    horarios = models.TextField()

class Tutoria(models.Model):
    tutor = models.CharField(max_length=100)
    ramos_que_domina = models.TextField()
    email = models.EmailField()