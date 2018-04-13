from django.contrib import admin
from .models import Event
from new_music.models import MainGenre, SubGenre


class PossMainGenre(admin.TabularInline):
    model = MainGenre

class PossMainGenreAdmin(admin.ModelAdmin):
    inlines = (PossMainGenre, )

class PossSubGenre(admin.TabularInline):
    model = SubGenre

class PossSubGenreAdmin(admin.ModelAdmin):
    inlines = (PossSubGenre, )
    
# Register your models here.
admin.site.register(Event)