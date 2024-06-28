from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Paquete(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField()
    precio = models.PositiveBigIntegerField()
    disponibilidad = models.BooleanField()
    codigo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    fecha_llegada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    hora_llegada = models.TimeField()
    hora_salida = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva de {self.usuario.username} del {self.fecha_llegada} al {self.fecha_salida}"

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 