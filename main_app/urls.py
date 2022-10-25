from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.PokemonList.as_view(), name="pokemon_index"),
    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(), name='pokemon_detail'),
    path('pokemon/create', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('items/', views.ItemList.as_view(), name='item_index'),
]
