from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^main$', get_mainpage_index, name='mainpage'),
    url(r'^new_main$', new_main_genre, name='new_main'),
    url(r'^genre/(\d+)$', genre_description, name='genre_desc')
]
