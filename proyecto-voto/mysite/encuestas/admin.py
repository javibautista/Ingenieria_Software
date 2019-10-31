from django.contrib import admin

from .models import Opcion, Pregunta

admin.site.register(Pregunta)
admin.site.register(Opcion)
