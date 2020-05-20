from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NewsArticoliModel,NewsGiornalistiModel
# Create your views here.
class listaPostView(ListView):
    model = NewsArticoliModel #modello dei dati da utilizzare 
    template_name = "news/lista_articoli.html"  #pagina per mostrare i dati

class listaGiornalistiView(ListView):
    model = NewsGiornalistiModel #modello dei dati da utilizzare 
    template_name = "news/lista_giornalisti.html"  #pagina per mostrare i dati




