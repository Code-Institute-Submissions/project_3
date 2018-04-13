from django import forms
from .models import Event

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'country', 'address', 'date', 'max_people', 'people_going', 'currency', 'admission', 'genre', 'subgenre')
        