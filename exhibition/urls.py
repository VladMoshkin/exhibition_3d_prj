from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.exhibition_list, name='exhibition_list'),
    url(r'^exhibition/(?P<pk>\d+)/$', views.exhibition_detail, name='exhibition_detail'),
    url(r'^about/', views.about, name='about')
]
