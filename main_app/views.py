from django.shortcuts import render
from .models import Pokemon
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class PokemonList(ListView):
    model = Pokemon
    pokemon = Pokemon.objects.all()

class PokemonDetailView(DetailView):
    model = Pokemon
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context['pokemon_list'] = Pokemon.objects.all()
        return context
    
class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'description', 'lvl']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'
    