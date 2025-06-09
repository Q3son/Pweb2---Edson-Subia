
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event-detail'),
    path('ticket/<int:event_id>/pdf/', views.generate_ticket_pdf, name='ticket-pdf'),
    path('ticket/<int:event_id>/pdf/download/', views.generate_ticket_pdf, {'download': True}, name='ticket-pdf-download'),
    # NUEVA URL para el correo
    path('event/<int:event_id>/send-email/', views.send_confirmation_email, name='send-email'),
]