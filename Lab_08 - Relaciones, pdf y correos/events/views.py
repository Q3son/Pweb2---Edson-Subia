from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Event
from .utils import render_to_pdf # Importamos nuestra función de utilidad

def generate_ticket_pdf(request, event_id):
    """
    Genera un PDF para un ticket de un evento específico.
    """
    # Obtenemos el evento de la base de datos, o un error 404 si no existe
    event = get_object_or_404(Event, pk=event_id)
    
    # Preparamos el contexto que se pasará a la plantilla HTML
    context = {
        'event': event,
        'user': request.user,
    }
    
    # Llamamos a nuestra función de utilidad
    pdf = render_to_pdf('events/ticket_pdf.html', context)
    
    # Si la función devolvió un PDF, lo servimos.
    # HttpResponse se encarga del resto.
    if pdf:
        response = pdf
        # Opcional: Forzar la descarga en lugar de mostrar en el navegador
        # filename = f"ticket_{event.id}.pdf"
        # content = f"attachment; filename={filename}"
        # response['Content-Disposition'] = content
        return response
    
    return HttpResponse("Error al generar el PDF.", status=400)