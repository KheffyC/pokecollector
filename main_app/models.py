from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

BATTLES = (
    ('W', 'vs Wild Pokemon'),
    ('C', 'vs Civilian'),
    ('G', 'vs Gym Leader'),
    ('T', 'vs Trainer')
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lvl = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"pk": self.id})
    
    def train_for_today(self):
        return self.training_set.filter(date=date.today()).count() >= len(BATTLES) - 2
    
class Training(models.Model):
    date = models.DateTimeField('training time')
    battle = models.CharField(
        max_length=1,
        choices=BATTLES,
        default=BATTLES[0][0]
    )
    
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_battle_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
        
        

class Item(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.id})
    