from django.shortcuts import render
from django.views.generic import TemplateView
from publication.models import Publication

def home(request):
    publicaciones = Publication.objects.all()

    return render(request, 'publication/index.html',{'publicaciones':publicaciones})

class HomeView(TemplateView):
    template_name = 'sitio/index.html'

class AboutView(TemplateView):
    template_name = 'sitio/about.html'

class ContactView(TemplateView):
    template_name = 'sitio/contact.html'