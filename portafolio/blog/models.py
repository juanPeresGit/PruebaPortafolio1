from django.db import models
import datetime

 
# Create your models here.

class Post(models.Model):
    Titulo = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to="blog/images")
    Date = models.DateField(datetime.date.today)