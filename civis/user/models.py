from django.db import models

# Create your models here.
class Responses(models.Model):
    name=models.CharField(max_length=120)
    img=models.ImageField(upload_to='pics')