from django import forms
from .models import Livre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['ISBN','nom','auteur','stock']
        labels = {
            'ISBN' : 'ISBN',
            'nom' : 'nom',
            'auteur' : 'auteur',
            'stock' : 'stock'
        }
