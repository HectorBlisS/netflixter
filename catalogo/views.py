from django.shortcuts import render
from .models import Pelicula
from django.views.generic import View
from django.utils.text import slugify
from django.views.generic import View
class DetailMovie(View):
	def get(self, request,slug):
		template_name = 'detailmovie.html'
		detalle = get_object_or_404(Pelicula,slug=slug)
		context = {
		'detalle':detalle,
		}
		return render(request,template_name,context)
