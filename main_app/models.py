from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.TextField(max_length=250)
    lvl = models.IntegerField()