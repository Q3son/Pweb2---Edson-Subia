from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from .models import Event
from django.conf import settings
from .utils import render_to_pdf # Importamos nuestra función de utilidad

def generate_ticket_pdf(request, event_id):
    """
    Genera un PDF para un ticket de evento y envía un correo de confirmación
    con el PDF adjunto.
    """
    event = get_object_or_404(Event, pk=event_id)
    
    context = {
        'event': event,
        'user': request.user,
    }
    
    # 1. Generamos el PDF en memoria como antes
    pdf_buffer = render_to_pdf('events/ticket_pdf.html', context)
    
    # Si la generación del PDF falla, retornamos un error.
    if pdf_buffer is None:
        return HttpResponse("Error al generar el PDF.", status=500)

    # Obtenemos el contenido del PDF desde el buffer en memoria
    pdf_content = pdf_buffer.getvalue()

    # 2. Componemos y enviamos el correo electrónico
    try:
        subject = f"Confirmación y Ticket para: {event.name}"
        body = (
            f"Hola {request.user.first_name},\n\n"
            f"¡Gracias por registrarte en nuestro evento '{event.name}'!\n\n"
            "Adjuntamos tu ticket en formato PDF. Por favor, guárdalo para el día del evento.\n\n"
            "¡Nos vemos pronto!\n"
            "El equipo de MyClub"
        )
        
        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            ['esubiahu@unsa.edu.pe'], # Lista de correos de los destinatarios
        )
        
        # Adjuntamos el PDF
        filename = f"ticket_{event.id}_{request.user.username}.pdf"
        email.attach(filename, pdf_content, 'application/pdf')
        email.send()

    except Exception as e:
        # En un caso real, aquí registraríamos el error en un sistema de logging.
        print(f"Error al enviar el correo: {e}")
        # No detenemos la respuesta del PDF aunque el correo falle.
        pass

    # 3. Servimos el PDF al usuario en el navegador como antes
    return HttpResponse(pdf_content, content_type='application/pdf')