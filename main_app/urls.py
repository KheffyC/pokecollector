from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name="index"),
    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(), name='detail'),
]
