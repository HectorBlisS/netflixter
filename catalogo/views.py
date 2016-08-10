from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Categoria 
from django.views.generic import View


# Create your views here.
class ListView(View):
    def get(self, request):
        template_name = 'catalogos/lista.html'
        peliculas = Pelicula.objects.all()
        context = {
        'peliculas':peliculas,
        }
        return render(request,template_name,context)

class DetailView(View):
    def get(self, request, slug):
        template_name = 'catalogos/detalle.html'
        #pelicula = get_list_or_404(Pelicula,slug=slug)
        pelicula = Pelicula.objects.get(slug=slug)
        context = {
        'pelicula':pelicula,
        }
        return render(request,template_name,context)

class Categorias(View):
    def get(self, request, categoria=None):
        if categoria:
            cat=Categoria.objects.get(nombre=categoria)
            peliculas = cat.objects.all()
        else:
            peliculas = Pelicula.objects.all()
        template_name = 'catalogos/lista.html'
        context = {
        'peliculas':peliculas,
        'categoria':categoria,
        }
        return render (request, template_name, context)
