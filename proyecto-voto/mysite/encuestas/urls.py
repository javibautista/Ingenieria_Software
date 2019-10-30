from django.urls import path
#importa el views.py que esta en este mismo directorio "."
from . import views

app_name = 'encuestas'
urlpatterns = [
    # views: vistas, index: indice
    # http://127.0.0.1:8000/encuestas/ --> °¿Que es Django?
    # http://127.0.0.1:8000/encuestas/1/  --> Estás mirando la pregunta 1.
    path('', views.indice, name='indice'),
    # http://127.0.0.1:8000/encuestas/5/
    # the 'name' value as called by the {% url %} template tag
    # el valor 'nombre' como lo llama {% url %} la etiqueta de plantilla
    path('<int:pregunta_id>/', views.detalle, name='detalle'),
    # http://127.0.0.1:8000/encuestas/5/resultados/
    path('<int:pregunta_id>/resultados/', views.resultados, name='resultados'),
    # http://127.0.0.1:8000/encuestas/5/votar/
    path('<int:pregunta_id>/votar/', views.votar, name='votar'),
]
