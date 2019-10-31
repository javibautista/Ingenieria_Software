import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Opcion, Pregunta


class PreguntaModelTests(TestCase):

    def test_was_published_recently_with_future_pregunta(self):
        """
        was_published_recently() returns False for preguntas whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_pregunta = Pregunta(pub_date=time)
        self.assertIs(future_pregunta.was_published_recently(), False)
        
    def test_was_published_recently_with_old_pregunta(self):
        """
        was_published_recently() returns False for preguntas whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_pregunta = Pregunta(pub_date=time)
        self.assertIs(old_pregunta.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_pregunta(self):
        """
        was_published_recently() returns True for preguntas whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_pregunta = Pregunta(pub_date=time)
        self.assertIs(recent_pregunta.was_published_recently(), True)
        
def create_pregunta(pregunta_text, days):
    """
    Create a pregunta with the given `pregunta_text` and published the
    given number of `days` offset to now (negative for preguntas published
    in the past, positive for preguntas that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Pregunta.objects.create(pregunta_text=pregunta_text, pub_date=time)
    
    
class PreguntaIndexViewTests(TestCase):
    def test_no_preguntas(self):
        """
        If no preguntas exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('encuestas:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No encuestas are available.")
        self.assertQuerysetEqual(response.context['latest_pregunta_list'], [])

    def test_past_pregunta(self):
        """
        Preguntas with a pub_date in the past are displayed on the
        index page.
        """
        create_pregunta(pregunta_text="Past pregunta.", days=-30)
        response = self.client.get(reverse('encuestas:index'))
        self.assertQuerysetEqual(
            response.context['latest_pregunta_list'],
            ['<Pregunta: Past pregunta.>']
        )

    def test_future_pregunta(self):
        """
        Preguntas with a pub_date in the future aren't displayed on
        the index page.
        """
        create_pregunta(pregunta_text="Future pregunta.", days=30)
        response = self.client.get(reverse('encuestas:index'))
        self.assertContains(response, "No encuestas are available.")
        self.assertQuerysetEqual(response.context['latest_pregunta_list'], [])

    def test_future_pregunta_and_past_pregunta(self):
        """
        Even if both past and future preguntas exist, only past preguntas
        are displayed.
        """
        create_pregunta(pregunta_text="Past pregunta.", days=-30)
        create_pregunta(pregunta_text="Future pregunta.", days=30)
        response = self.client.get(reverse('encuestas:index'))
        self.assertQuerysetEqual(
            response.context['latest_pregunta_list'],
            ['<Pregunta: Past pregunta.>']
        )

    def test_two_past_preguntas(self):
        """
        The preguntas index page may display multiple preguntas.
        """
        create_pregunta(pregunta_text="Past pregunta 1.", days=-30)
        create_pregunta(pregunta_text="Past pregunta 2.", days=-5)
        response = self.client.get(reverse('encuestas:index'))
        self.assertQuerysetEqual(
            response.context['latest_pregunta_list'],
            ['<Pregunta: Past pregunta 2.>', '<Pregunta: Past pregunta 1.>']
        )
        
class PreguntaDetailViewTests(TestCase):
    def test_future_pregunta(self):
        """
        The detail view of a pregunta with a pub_date in the future
        returns a 404 not found.
        """
        future_pregunta = create_pregunta(pregunta_text='Future pregunta.', days=5)
        url = reverse('encuestas:detail', args=(future_pregunta.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_pregunta(self):
        """
        The detail view of a pregunta with a pub_date in the past
        displays the pregunta's text.
        """
        past_pregunta = create_pregunta(pregunta_text='Past Pregunta.', days=-5)
        url = reverse('encuestas:detail', args=(past_pregunta.id,))
        response = self.client.get(url)
        self.assertContains(response, past_pregunta.pregunta_text)
