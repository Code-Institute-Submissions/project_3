from django.db import models
from django_countries.fields import CountryField
from new_music.models import MainGenre, SubGenre

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, blank=False, help_text='Name of the event.')
    description = models.TextField(max_length=800, blank=False, help_text='What is happening at the event?')
    date = models.DateTimeField(auto_now=False, help_text='Year-Month-Day Time (2018-03-22 22:30 = March 22, 2018, 10:30PM), Time is in 24 hour time!')
    posttime = models.DateTimeField(auto_now=True)
    country = CountryField()
    address = models.CharField(max_length=400, blank=False, help_text='Where is the event?')
    max_people = models.IntegerField(blank=False, help_text='How many people are allowed?') 
    people_going = models.IntegerField(blank=False, default=0, help_text='How many people are already going?')
    currency = models.CharField(max_length=4, blank=False, default='EUR', help_text='What currency is it? IE. USD, EUR, GBP ect.') 
    admission = models.DecimalField(max_digits=8, decimal_places=2, blank=False, default=0.00, help_text='Is there a cost to enter?')
    genre = models.ForeignKey(MainGenre, null=True, blank=True)
    subgenre = models.ForeignKey(SubGenre, null=True, blank=True)
    
    def __str__(self):
        return self.name