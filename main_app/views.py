from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Pokemon:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
    
pokemon = [
    Pokemon('Bulbasaur', 'Grass', 10),
    Pokemon('Arcanine', 'Fire', 35),
    Pokemon('Dratini', 'Dragon', 6),
]


def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })