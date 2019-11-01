import datetime

from django.db import models
from django.utils import timezone

# Question
class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicación')
    
    def __str__(self):
        return self.pregunta_text
    
    # fue_publicado_recientemente
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

# Choice
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    #votos = models.IntegerField(default=0)
    correcto = models.BooleanField(default=False)
    
    def __str__(self):
        return self.opcion_text
