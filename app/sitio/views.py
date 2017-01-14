from django.shortcuts import render
from publication.models import Publication

def home(request):
    publicaciones = Publication.objects.all()

    return render(request, 'publication/index.html',{'publicaciones':publicaciones})
