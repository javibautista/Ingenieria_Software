from django.http import HttpResponse

from django.template import loader

from .models import Pregunta

# index: indice, question: pregunta
def indice(request):
    # latest_question_list: ultima_pregunta_lista
    ultima_pregunta_lista = Pregunta.objects.order_by('-pub_fecha')[:5]
    # template: plantilla
    plantilla = loader.get_template('encuestas/indice.html')
    # context: context
    contexto = {
        'ultima_pregunta_lista': ultima_pregunta_lista,
    }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(plantilla.render(contexto, request))

# detail: detalle
def detalle(request, pregunta_id):
    return HttpResponse("Estás mirando la pregunta %s." % pregunta_id)

# results: resultados, response: respuesta
def resultados(request, pregunta_id):
    respuesta = "Estás viendo los resultados de la pregunta %s."
    return HttpResponse(respuesta % pregunta_id)

# vote: voto
def voto(request, pregunta_id):
    return HttpResponse("Estás votando una pregunta %s." % pregunta_id)


