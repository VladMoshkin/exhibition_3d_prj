from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('exhibition.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
