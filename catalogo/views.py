from django.shortcuts import render, get_list_or_404
from .models import Pelicula
from django.views.generic import View
from django.utils.text import slugify


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

