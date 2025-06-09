from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_path: str, context: dict = {}):
    """
    Renderiza una plantilla HTML de Django a un objeto PDF.
    
    :param template_path: Ruta a la plantilla HTML.
    :param context: Un diccionario de contexto para pasar a la plantilla.
    :return: Un objeto HttpResponse con el PDF, o None si hay un error.
    """
    template = get_template(template_path)
    html = template.render(context)
    result = BytesIO() # Un buffer en memoria para el PDF

    # Creamos el PDF
    pdf_status = pisa.CreatePDF(
        html.encode("ISO-8859-1"), # El HTML a convertir
        dest=result             # El objeto de archivo donde se guardará (nuestro buffer)
    )

    # Si hay un error, pisa devuelve True en pdf.err
    if pdf_status.err:
        return None

    # Si todo va bien, devolvemos el HttpResponse con el tipo de contenido correcto
    return result