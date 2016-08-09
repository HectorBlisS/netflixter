from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
