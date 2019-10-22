from django.urls import path
#importa el views.py que esta en este mismo directorio "."
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
