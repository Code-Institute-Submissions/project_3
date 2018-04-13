from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from home.views import *
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', render_homepage, name='home'),
    url(r'^about$', render_aboutpage, name='about'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^messenger/', include('messenger.urls')),
    url(r'^groove/', include('new_music.urls')),
    url(r'^locate/', include('locate_music.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)