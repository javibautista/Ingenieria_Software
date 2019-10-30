import datetime

from django.db import models
from django.utils import timezone

# Question
class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('fecha de publicación')
    
    def __str__(self):
        return self.pregunta_text
    
    # was_published_recently
    def fue_publicado_recientemente(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)

# Choice
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.opcion_text
