from django.db import models 
from django.db.models.fields.files import ImageField
from django.db.models.fields import  CharField, URLField



# Create your models here.

class Project(models.Model):
    Titulo = CharField(max_length=100)
    Descripcion = CharField(max_length=200)
    Imagen = ImageField(upload_to="portafolio/images/")
    Url = URLField(blank=True)