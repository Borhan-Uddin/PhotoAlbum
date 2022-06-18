from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)


    def __str__(self):
        return self.name


class Photo(models.Model):
    description = models.TextField(null=False, blank=False)
    image = CloudinaryField('image',null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.description[:20]
