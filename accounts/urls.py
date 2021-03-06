from django.conf.urls import url, include
from .views import *
from . import urls_reset

urlpatterns = [
    url(r'^login$', account_login, name="login"),
    url(r'^logout', logout, name="logout"),
    url(r'^profile', account_profile, name="profile"),
    url(r'^register', register_new_account, name="register"),
    url(r'^password-reset/', include(urls_reset)),
]
