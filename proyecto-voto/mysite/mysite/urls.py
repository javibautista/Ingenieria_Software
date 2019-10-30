from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # url: /encuestas, app: encuestas/urls
    path('encuestas/', include('encuestas.urls')),
    path('admin/', admin.site.urls),
]
