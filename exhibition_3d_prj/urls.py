from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from exhibition import views
#from accounts import views as acc_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('exhibition.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^account/', include('accounts.urls')),
    url(r'^addimage/', include('image.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
