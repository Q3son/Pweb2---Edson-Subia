# personas/urls.py
from django.urls import path
from . import views

app_name = 'personas'
urlpatterns = [
    path('contactos/', views.lista_contactos, name='lista'),
    path('contactos/<int:id>/', views.detalle_contacto, name='detalle'),
]