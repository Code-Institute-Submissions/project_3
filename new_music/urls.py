from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^main$', get_mainpage_index, name='mainpage'),
    url(r'^new_main$', new_main_genre, name='new_main'),
    url(r'^new_artist$', new_artist, name='new_artist'),
    url(r'^new_subgenre$', new_subgenre, name='new_subgenre'),
    url(r'^genre/(\d+)$', genre_description, name='genre_desc'),
    url(r'^subgenre/(\d+)$', subgenre_description, name='subgenre_desc'),
    url(r'^artist/(\d+)$', artist_description, name='artist_desc'),
]
