from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Opcion, Pregunta

# index: indice, pregunta: pregunta
class IndiceView(generic.ListView):
    template_name = 'indice.html'
    context_object_name = 'ultima_pregunta_lista'

    # get_queryset: obtener conjunto de consultas
    def get_queryset(self):
        """Devuelva las últimas cinco preguntas publicadas."""
        return Pregunta.objects.order_by('-pub_fecha')[:5]

# detail: detalle
class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/detalle.html'

# results: resultados, response: respuesta
class ResultadosView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/resultados.html'

# vote: voto
def voto(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Vuelva a mostrar el formulario de votación de preguntas.
        return render(request, 'encuestas/detalle.html', {
            'pregunta': pregunta,
            'error_message': "No seleccionaste una opción.",
        })
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        # Siempre devuelva un HttpResponseRedirect después de tratar con éxito
        # los datos POST. Esto evita que los datos se publiquen dos veces si un
        # usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(pregunta.id,)))


