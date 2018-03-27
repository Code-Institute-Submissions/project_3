from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^login$', account_login, name="login"),
    url(r'^logout', logout, name="logout"),
    url(r'^profile', account_profile, name="profile"),
    url(r'^register', register_new_account, name="register"),
]
