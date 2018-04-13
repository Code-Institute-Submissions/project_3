from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^events$', get_events_index, name='events'),
    url(r'^date_events$', date_sorted_events, name='date_events'),
    url(r'^admission_events$', admission_sorted_events, name='admission_events'),
    url(r'^new_event$', new_event, name='new_event'),
    url(r'^event/(\d+)$', event_desc, name='event_desc'),
]