from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^registro/$', views.Registro.as_view(), name="registro"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
]