from django.db import models
from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lvl = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"pk": self.id})


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("toy_detail", kwargs={"pk": self.id})
    