from django.urls import path
from . import views

from django.urls import path
from .views import (
    DestinoListView, 
    DestinoDetailView,
    DestinoCreateView,
    DestinoUpdateView,
    DestinoDeleteView
)

urlpatterns = [
    path('', DestinoListView.as_view(), name='list_destinos'),
    path('add/', DestinoCreateView.as_view(), name='add_destino'),
    path('<int:pk>/', DestinoDetailView.as_view(), name='detail_destino'),
    path('<int:pk>/edit/', DestinoUpdateView.as_view(), name='edit_destino'),
    path('<int:pk>/delete/', DestinoDeleteView.as_view(), name='delete_destino'),
]