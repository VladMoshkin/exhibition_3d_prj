from django.conf.urls import url
from . import views
from image.views import addimage

urlpatterns = [
    url(r'^$', views.exhibition_list, name='exhibition_list'),
    url(r'^exhibitions/$', views.exhibition_list_grid, name='exhibition_list_grid'),
    url(r'^exhibitions/addimage/$', views.exhibition_addimage, name='exhibition_addimage'),
    url(r'^exhibitions/(?P<pk>\d+)/$', views.exhibition_detail, name='exhibition_detail'),
    url(r'^exhibitions/(?P<pk>\d+)/addimage/$', addimage, name='addimage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^vacantion/$', views.vacantion, name='vacantion'),
]
