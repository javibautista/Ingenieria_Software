from django.http import HttpResponse

# index: indice, question: pregunta
def indice(request):
    return HttpResponse("Hola Mundo. Estás en el index(índice) de encuestas.")

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


