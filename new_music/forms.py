from django import forms
from .models import MainGenre, SubGenre

class MainGenreForm(forms.ModelForm):
    class Meta:
        model = MainGenre
        fields = ('name', 'description', 'image')
        
class SubGenreForm(forms.ModelForm):
    class Meta:
        model = SubGenre
        fields = ('dom', 'name', 'description', 'image')