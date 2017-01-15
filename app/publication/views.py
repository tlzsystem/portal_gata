from django.views.generic import ListView, DetailView
from .models import Publication

class ListaPublications(ListView):
    paginate_by = 10
    queryset = Publication.objects.order_by('-date_published')

class DetailPublication(DetailView):
    model = Publication


