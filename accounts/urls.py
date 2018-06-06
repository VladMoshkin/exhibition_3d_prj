from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', views.logout_user, name="logout")
]
