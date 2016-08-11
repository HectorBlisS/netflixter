from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from main import urls as UrlsMain

from catalogo import urls as catalogoUrls
from django.views.static import serve
from accounts import urls as urlsAccounts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urlsAccounts)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^catalogo/',include(catalogoUrls,namespace="catalogo")),
    url(
        regex=r'^media/(?P<path>.*)$',

        view= serve,

        kwargs={'document_root':settings.MEDIA_ROOT}),
    url(r'^', include(UrlsMain,namespace="home")),      
]
