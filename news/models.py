from django.db import models

# Create your models here.
class NewsGiornalistiModel(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class NewsArticoliModel(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    autore = models.ForeignKey(NewsGiornalistiModel, on_delete=models.CASCADE, related_name="articoli",default=1,)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"


