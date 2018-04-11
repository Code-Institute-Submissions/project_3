from django.contrib import admin
from .models import MainGenre, SubGenre

# Register your models here.
admin.site.register(MainGenre)
admin.site.register(SubGenre)