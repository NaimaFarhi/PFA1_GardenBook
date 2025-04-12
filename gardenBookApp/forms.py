from django import forms
from .models import Livre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','email','password1','password2']