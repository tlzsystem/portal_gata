from django.db import models
from category.models import Category, Type

class Publication(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=20)
    date_published = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    type = models.ForeignKey(Type)

    class Meta:
        verbose_name_plural = "Publications"

        def __str__(self):
            return '%s'%(self.title)


class PublicationImage(models.Model):
    publication = models.ForeignKey(Publication)
    image = models.ImageField(upload_to='publication/images/')

    def __str__(self):
        return str(self.image)





