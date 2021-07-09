from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Sistema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

class Smartphone(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=99)
    sistema = models.ForeignKey(Sistema, on_delete=CASCADE)
    