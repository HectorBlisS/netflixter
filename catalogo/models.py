from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.TextField()
    director = models.CharField(max_length = 50)
    escritor = models.CharField(max_length = 50)
    estudio = models.CharField(max_length = 30)
    genero = models.CharField(max_length = 20)
    year = models.IntegerField()
    duracion = models.IntegerField()
    clasificacion = models.CharField(max_length = 15)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pelicula = models.ManyToManyField(Pelicula)

    def __str__(self):
        return self.nombre
