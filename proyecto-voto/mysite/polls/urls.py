from django.urls import path
from . import views

from .views import (SocialLoginView)

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/corregir/', views.corregir, name='corregir'),
    #path('', SocialLoginView(template_name='polls/allauth.html')),
    path('oauth/login/', SocialLoginView.as_view()),
]
