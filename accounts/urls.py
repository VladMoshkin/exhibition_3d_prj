from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^enter', login, {'template_name': 'pages/accounts/enter.html'}),
    url(r'', views.profile, name='profile')
]