from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NewsArticoliModel,NewsGiornalistiModel
from django.shortcuts import get_object_or_404

# Create your views here.
class listaPostView(ListView):
    model = NewsArticoliModel #modello dei dati da utilizzare 
    template_name = "news/lista_articoli.html"  #pagina per mostrare i dati

class listaGiornalistiView(ListView):
    model = NewsGiornalistiModel #modello dei dati da utilizzare 
    template_name = "news/lista_giornalisti.html"  #pagina per mostrare i dati

def listaArticoliGiornalistaView(request,pk):
    giornalista=get_object_or_404(NewsGiornalistiModel, id=pk)
    articoli=giornalista.articoli.all()
    context = {'giornalista': giornalista,
               'newsarticolimodel_list': articoli,
               }
    return render(request, 'news/lista_articoli.html', context)



