from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo. Estás en el index(índice) de encuestas.")
