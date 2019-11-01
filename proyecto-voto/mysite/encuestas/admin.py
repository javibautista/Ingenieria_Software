from django.contrib import admin

from .models import Opcion, Pregunta

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pregunta_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [OpcionInline]
    list_display = ('pregunta_text', 'pub_date')

admin.site.register(Pregunta, PreguntaAdmin)
