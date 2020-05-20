from django import forms
from .models import NewsArticoliModel,NewsGiornalistiModel


class NewsArticoliModelForm(forms.ModelForm):

    class Meta:
        model = NewsArticoliModel
        fields = "__all__"

class NewsGiornalistiModelForm(forms.ModelForm):

    class Meta:
        model = NewsGiornalistiModel
        fields = "__all__"
