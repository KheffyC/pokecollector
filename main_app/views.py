from django.shortcuts import render
from .models import Pokemon
from django.views.generic.detail import DetailView

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

class PokemonDetailView(DetailView):
    model = Pokemon
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context['pokemon_list'] = Pokemon.objects.all()
        return context