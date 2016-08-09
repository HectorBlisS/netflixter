<<<<<<< HEAD
from django shortcuts import render, redirect 
from django.views.generic import View 
from .models import Profile 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 

from .forms import RegisterForm, UserEditForm

class Dashboard(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "accounts/profile.html"
		userform = UserEditForm(instance=request.user)
		if userform.is_valid():
			userform.save()
			return redirect('profile')
		else: 
			context={
			'userform':userform,
			}
			return render(request,template_name,context)

class Registration(View):
	def get(self,request):
		template_name = #"FAAAAAAAAAALTAAAAA"
		form = UserRegistrationForm()
		context = {
=======
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
>>>>>>> 9f7ae6616766d02d5b8c480de7bc3f85628e92e1
		'form':form,
		}
		return render(request,template_name,context)

<<<<<<< HEAD
	def BIIIIIAAAATCH(self,request):
		template_name = #"FAAAAAAAALTAAAAAA"
		new_user_form = UserRegistrationForm(request.--POST--)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
=======
	def post(self,request):
		template_name = "accounts/registro.html"
		new_user_form = RegistroUsuario(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
>>>>>>> 9f7ae6616766d02d5b8c480de7bc3f85628e92e1
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
<<<<<<< HEAD
			return redirect('profile')
=======
			# perfil = Profile.objects.create(user=new_user)
			return redirect('registro')
>>>>>>> 9f7ae6616766d02d5b8c480de7bc3f85628e92e1
		else:
			context = {
			'form':new_user_form
			}
<<<<<<< HEAD
			return render(request,template_name,context)
=======
			return render(request,template_name,context)
>>>>>>> 9f7ae6616766d02d5b8c480de7bc3f85628e92e1
