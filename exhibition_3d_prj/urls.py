from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from exhibition import views
from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('exhibition.urls')),
    url(r'^account/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^api/submit/$', views.submit, name="submit"),
    url(r'^api/change/user/$', views.change_user, name="change_user"),
    url(r'^api/change/user-info/$', views.change_userinfo, name="change_userinfo"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
