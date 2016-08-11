from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categoria/(?P<categoria>[-w]+)/$', views.Categorias.as_view(), name="categoria"),
    url(r'^$', views.ListView.as_view(), name='lista'),
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detalle'),
]

