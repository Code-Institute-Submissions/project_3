from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^events$', get_events_index, name='events'),
    url(r'^new_event$', new_event, name='new_event')
]