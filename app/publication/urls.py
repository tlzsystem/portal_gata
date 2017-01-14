from django.conf.urls import url
from .views import ListaPublications, DetailPublication

urlpatterns = [
    url(r'^publications/$', ListaPublications.as_view() ,name='lista-publicaciones'),
    url(r'^publications/(?P<pk>[0-9]+)/$', DetailPublication.as_view() ,name='detalle-publicacion'),
]
