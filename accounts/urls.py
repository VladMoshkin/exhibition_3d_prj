from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^register/$', views.register, name="register"),
]
