from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Opcion, Pregunta

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

# index: indice, pregunta: pregunta
class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'latest_pregunta_list'

    # get_queryset: obtener conjunto de consultas
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Pregunta.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# detail: detalle
class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Pregunta.objects.filter(pub_date__lte=timezone.now())

# results: resultados, response: respuesta
class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/results.html'

# vote: voto
def voto(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Vuelva a mostrar el formulario de votación de preguntas.
        return render(request, 'encuestas/detail.html', {
            'pregunta': pregunta,
            'error_message': "No seleccionaste una opción.",
        })
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        # Siempre devuelva un HttpResponseRedirect después de tratar con éxito
        # los datos POST. Esto evita que los datos se publiquen dos veces si un
        # usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse('encuestas:results', args=(pregunta.id,)))


