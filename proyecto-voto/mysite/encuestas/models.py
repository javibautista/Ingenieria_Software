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

# Choice
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.opcion_text
