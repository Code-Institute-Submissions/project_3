from django.contrib import admin
from .models import MainGenre, SubGenre, Artists

# Register your models here.
admin.site.register(MainGenre)
admin.site.register(SubGenre)
admin.site.register(Artists)