from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuario, ProfileEditForm

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		# userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		#'userform':userform,
		'profileform':profileform,
		}
		return render(request,template_name,context)
	def perf(self,request):
		template_name="accounts/perfil.html"
		# userform = UserEditForm(instance=request.user,data=request.POST)
		profileform = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
		if profileform.is_valid():
			# userform.save()
			profileform.save()
			return redirect('profile')
		else:
			context={
			# 'userform':userform,
			'profileform':profileform,
			}
			return render(request,template_name,context)
		


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
			return redirect('profile')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)

