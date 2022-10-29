from xml.etree.ElementInclude import include
from django.urls import URLPattern, path

from . import views

URLPattern - {
    path('', views.index, name='index'),
    path('', include('musicapp.urls')),
}