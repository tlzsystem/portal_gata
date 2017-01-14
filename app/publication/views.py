from django.views.generic import ListView, DetailView
from .models import Publication

class ListaPublications(ListView):
    queryset = Publication.objects.order_by('-date_published')

class DetailPublication(DetailView):
    model = Publication


