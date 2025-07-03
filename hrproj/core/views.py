import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from .models import Employee

def link_callback(uri, rel):
    """
    Преобразует URI статических/медиа-файлов в абсолютный путь на диске.
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = finders.find(uri.replace(settings.STATIC_URL, ""))
    else:
        return uri  # обычный URI
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path

def employee_card_pdf(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    html = render_to_string('core/employee_card.html', {'employee': employee})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="employee_{employee.pk}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
