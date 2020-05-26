from django.urls import path
from . import views
from .views import listaPostView,listaGiornalistiView,listaArticoliGiornalistaView

app_name = 'news'
urlpatterns = [
    path('lista-articoli', listaPostView.as_view(), name='lista_articoli'),
    path('lista-giornalisti',listaGiornalistiView.as_view(), name='lista_giornalisti'),
    path('lista-articoli-giornalista/<int:pk>', listaArticoliGiornalistaView, name='lista_articoli_giornalista'),
]