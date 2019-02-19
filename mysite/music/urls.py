from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AliciaKeys', views.AliciaKeys, name='index'),
    path('JCole', views.JCole, name='index'),
    path('Tupac', views.Tupac, name='index'),
]