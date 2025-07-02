from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from .models import Employee

def employee_card_pdf(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    html = render_to_string('core/employee_card.html', {'employee': employee})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="employee_{employee.pk}.pdf"'

    # конвертируем HTML в PDF и пишем прямо в response
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
