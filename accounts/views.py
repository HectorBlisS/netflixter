from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from .forms import RegistroUsuario

# Create your views here.


class Registro(View):
	def get(self, request):
		template_name = "accounts/registro.html"
		form = RegistroUsuario()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registro.html"
		new_user_form = RegistroUsuario(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			# perfil = Profile.objects.create(user=new_user)
			return redirect('profile')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)
