from django.urls import path
#importa el views.py que esta en este mismo directorio "."
from . import views

app_name = 'encuestas'
urlpatterns = [
    # views: vistas, index: indice
    # http://127.0.0.1:8000/encuestas/ --> °¿Que es Django?
    # http://127.0.0.1:8000/encuestas/1/  --> Estás mirando la pregunta 1.
    path('', views.IndexView.as_view(), name='index'),
    # http://127.0.0.1:8000/encuestas/5/
    # the 'name' value as called by the {% url %} template tag
    # el valor 'nombre' como lo llama {% url %} la etiqueta de plantilla
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # http://127.0.0.1:8000/encuestas/5/resultados/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # http://127.0.0.1:8000/encuestas/5/voto/
    path('<int:pregunta_id>/voto/', views.voto, name='voto'),
]
