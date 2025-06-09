from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Importamos TODOS los modelos que usaremos en las vistas
from .models import Event, Language, Framework, Movie, Character 
from .utils import render_to_pdf

def home(request):
    context = {
        'event_list': Event.objects.all().order_by('event_date'),
        'language_list': Language.objects.all(),
        'framework_list': Framework.objects.all(),
        'movie_list': Movie.objects.all(),
        'character_list': Character.objects.all(),
    }
    return render(request, 'events/home.html', context)

def event_detail(request, event_id):
    """
    Vista para mostrar los detalles de un único evento,
    incluyendo sus asistentes.
    """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/event_detail.html', context)

def generate_ticket_pdf(request, event_id, download=False):
    """
    Vista unificada para generar un PDF.
    - Sirve el PDF en el navegador.
    - Opcionalmente, fuerza su descarga.
    - Opcionalmente (aunque no implementado aquí), puede enviar por correo.
    """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
        'user': request.user, # Asume que el usuario está logueado
    }
    
    # 1. Generamos el PDF usando nuestra función de utilidad
    pdf_buffer = render_to_pdf('events/ticket_pdf.html', context)
    
    # Si la generación falla, retornamos un error claro
    if pdf_buffer is None:
        return HttpResponse("Error al generar el PDF.", status=500)

    # 2. Obtenemos el contenido una sola vez
    pdf_content = pdf_buffer.getvalue()
    pdf_buffer.close()
    
    # 3. Creamos la respuesta HTTP
    response = HttpResponse(pdf_content, content_type='application/pdf')
    
    # 4. Si se solicita la descarga, añadimos la cabecera necesaria
    if download:
        filename = f"ticket_{event.id}_{request.user.username}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def send_confirmation_email(request, event_id):
    """
    Vista dedicada a enviar el correo de confirmación con el ticket adjunto.
    """
    event = get_object_or_404(Event, pk=event_id)
    user = request.user # Asume que el usuario está logueado
    
    # Generamos el PDF en memoria para adjuntarlo
    context = {'event': event, 'user': user}
    pdf_buffer = render_to_pdf('events/ticket_pdf.html', context)
    
    if pdf_buffer:
        pdf_content = pdf_buffer.getvalue()
        pdf_buffer.close()
        
        # Componemos y enviamos el correo electrónico
        try:
            subject = f"Confirmación y Ticket para: {event.name}"
            body = (
                f"Hola {user.first_name},\n\n"
                f"¡Gracias por registrarte en nuestro evento '{event.name}'!\n\n"
                "Adjuntamos tu ticket en formato PDF.\n\n"
                "¡Nos vemos pronto!\nEl equipo de MyClub"
            )
            
            email = EmailMessage(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [user.email], # Enviamos al correo del usuario logueado
            )
            
            filename = f"ticket_{event.id}_{user.username}.pdf"
            email.attach(filename, pdf_content, 'application/pdf')
            email.send()
            
            # Devolvemos un mensaje de éxito
            return HttpResponse(f"¡Correo de confirmación enviado a {user.email} con éxito!")
            
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            return HttpResponse("Hubo un error al enviar el correo.", status=500)
            
    return HttpResponse("No se pudo generar el ticket para el correo.", status=500)