from django.urls import path
from . import views  # Importa tus vistas locales
from .views import (
    home,
    add_destino,
    list_destinos,
    edit_destino,
    delete_destino,
    detail_destino
)

urlpatterns = [
    path('', list_destinos, name='list_destinos'),
    path('add/', add_destino, name='add_destino'),
    path('<int:id>/', detail_destino, name='detail_destino'),
    path('<int:id>/edit/', edit_destino, name='edit_destino'),
    path('<int:id>/delete/', delete_destino, name='delete_destino'),
]