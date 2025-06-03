from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_destino, name='add_destino'),
    path('list/', views.list_destinos, name='list_destinos'),
    path('edit/<int:id>/', views.edit_destino, name='edit_destino'),
    path('delete/<int:id>/', views.delete_destino, name='delete_destino'),
    path('detail/<int:id>/', views.detail_destino, name='detail_destino'),
]