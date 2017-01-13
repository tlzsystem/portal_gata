from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return '%s'%(self.category_name)


class Type(models.Model):
    type_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Types"

    def __str__(self):
        return '%s'%(self.type_name)