from django.contrib import admin
from .models import Pelicula, Categoria

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Categoria)