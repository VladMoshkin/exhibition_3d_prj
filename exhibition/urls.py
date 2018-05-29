from django.conf.urls import url
from . import views
from image.views import addimage

urlpatterns = [
    url(r'^$', views.exhibition_list, name='exhibition_list'),
    url(r'^exhibitions/(?P<pk>\d+)/$', views.exhibition_detail, name='exhibition_detail'),
    url(r'^exhibitions/(?P<pk>\d+)/addimage/$', addimage, name='addimage'),
    url(r'^about/', views.about, name='about')
]
