from django.contrib import admin
from .models import Category, Type

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)