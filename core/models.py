from django.db import models

# Create your models here.

class Sport(models.Model):
    idSport = models.IntegerField(primary_key=True, verbose_name='id deporte')
    nameSport = models.CharField(max_length=100,verbose_name='Nombre Deporte')

    def __str__(self):
        return (self.nameSport)

class ComenUsuario(models.Model):
    idUser = models.CharField(max_length=70,primary_key=True, verbose_name='id usuario')
    nombreUser = models.CharField(max_length=70, verbose_name='Nombre del usuario')
    titulo = models.CharField(max_length=20, verbose_name='titulo tema')
    texto = models.TextField(verbose_name='texto del tema')
    correo =  models.CharField(max_length=70, verbose_name='Correo del usuario')
    deporte = models.ForeignKey(Sport, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.idUser)