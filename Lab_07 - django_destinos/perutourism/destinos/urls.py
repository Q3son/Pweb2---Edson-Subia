from django.urls import path
from . import views  # Importa tus vistas locales
app_name = 'destinos'
from .views import (
    home,
    add_destino,
    list_destinos,
    edit_destino,
    delete_destino,
    detail_destino
)

urlpatterns = [
    path('list/', views.list_destinos, name='list_destinos'), # Será accesible como /destinos/list/
    path('add/', views.add_destino, name='add_destino'),       # Será accesible como /destinos/add/
    path('<int:id>/', views.detail_destino, name='detail_destino'), # /destinos/1/
    path('<int:id>/edit/', views.edit_destino, name='edit_destino'), # /destinos/1/edit/
    path('<int:id>/delete/', views.delete_destino, name='delete_destino'), # /destinos/1/delete/
]