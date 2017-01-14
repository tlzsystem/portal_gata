from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('user','title','date_published','category','title')

admin.site.register( Publication, PublicationAdmin)
