
from django.urls import path
from . import views

urlpatterns = [
    # ... (otras urls que puedas tener) ...
    path('ticket/<int:event_id>/pdf/', views.generate_ticket_pdf, name='ticket-pdf'),
]