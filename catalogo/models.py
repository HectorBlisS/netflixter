from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.TextField()
    director = models.CharField(max_length = 50)
    escritor = models.CharField(max_length = 50)
    estudio = models.CharField(max_length = 30)
    year = models.IntegerField()
    duracion = models.IntegerField()
    clasificacion = models.CharField(max_length = 15)
    slug = models.SlugField(max_length=200)
    imagen = models.ImageField(upload_to='assets')

    def get_absolute_url(self):
        return reverse('catalogo:detalle',args=[self.slug])

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    pelicula = models.ManyToManyField(Pelicula)

    def __str__(self):
        return self.nombre

class Meta:
    ordering = ('-titulo')
