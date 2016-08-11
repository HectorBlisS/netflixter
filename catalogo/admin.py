from django.contrib import admin
from .models import Pelicula, Categoria




class Peliculas_Admin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('titulo',)}


admin.site.register(Pelicula, Peliculas_Admin)
admin.site.register(Categoria)
