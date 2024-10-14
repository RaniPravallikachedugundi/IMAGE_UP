from django.db import models

# Create your models her
class Image(models.Model):
    Photo=models.ImageField(upload_to="my_image")