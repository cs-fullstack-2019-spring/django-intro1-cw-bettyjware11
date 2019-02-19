from django.urls import path

from . import views
# these are the patterns that the info shold follow when the url is requested
urlpatterns = [
    path('', views.index, name='index'),
    path('AliciaKeys', views.AliciaKeys, name='index'),
    path('JCole', views.JCole, name='index'),
    path('Tupac', views.Tupac, name='index'),
]