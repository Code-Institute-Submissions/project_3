from django import forms
from .models import MainGenre, SubGenre, Artists

class MainGenreForm(forms.ModelForm):
    class Meta:
        model = MainGenre
        fields = ('name', 'description', 'image')
        
class SubGenreForm(forms.ModelForm):
    class Meta:
        model = SubGenre
        fields = ('dom', 'subname', 'subdescription', 'subimage')

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = ('name', 'description', 'genre', 'subgenre', 'image')