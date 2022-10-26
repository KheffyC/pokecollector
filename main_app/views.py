from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TrainingForm
from .models import Pokemon, Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# ---- POKEMON VIEW CBVS ----

class PokemonList(ListView):
    model = Pokemon

class PokemonDetailView(FormMixin, DetailView):
    model = Pokemon
    form_class = TrainingForm    

    def get_success_url(self):
        return reverse('pokemon_detail', kwargs={'pk': self.object.id})
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)
    
def add_training(request, pokemon_id):
    form = TrainingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_training = form.save(commit=False)
        new_training.pokemon_id = pokemon_id
        new_training.save()
    return redirect('pokemon_detail', pokemon_id)
    
class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'description', 'lvl']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'


#  ---- TOY VIEW CBV'S

class ItemList(ListView):
    model = Item

class ItemDetailView(DetailView):
    model = Item
    
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    
class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
    
class ItemDelete(DeleteView):
    model = Item
    success_url = '/pokemon/'