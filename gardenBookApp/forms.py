from django import forms
from .models import Livre,User
from django.contrib.auth.forms import UserCreationForm
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['ISBN', 'nom', 'auteur', 'dispo', 'pubDate','genres', 'nbPage', 'language','keywords','description','audience']
        labels = {
            'ISBN': 'ISBN',
            'nom': 'Book Title',
            'auteur': 'Author',
            'dispo': 'Disponibility',
            'genres':'Genre',
            'pubDate': 'Publication Date',
            'nbPage': 'Number of Pages',
            'language': 'Language',
            'keywords': 'Keywords',
            'description': 'Book Description',
            'audience': 'Target Audience',
        }
        widgets = {
            'pubDate': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Type keywords...'}),
            'language': forms.TextInput(attrs={'placeholder': 'e.g. English'}),
            'dispo': forms.CheckboxInput(attrs={
                'class': 'custom-checkbox',  
                'id': 'dispo',
                'aria-label': 'Check if the book is available'  
            }),
            'nbPage': forms.NumberInput(attrs={'placeholder': 'e.g. 300'}),
            'audience': forms.Select(choices=[
                ('Children', 'Children'),
                ('Young Adult', 'Young Adult'),
                ('Adult', 'Adult'),
            ]),
        }

class CustomUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'cin',
            'phone_number', 'dob', 'role', 'address', 'city', 'postal_code', 'country'
        ]