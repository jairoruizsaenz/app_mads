from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudCreateForm, SolicitudUpdateForm
from .utils import *
import datetime


def ListSolicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-created_at')
    context = { 'solicitudes':solicitudes, 'mensaje': 'Este es un mensaje de prueba' }
    return render(request, 'base/solicitud_list.html', context)


def CreateSolicitud(request):
    form = SolicitudCreateForm(request.POST or None)
    if form.is_valid():
        solicitud_nueva = form.save()
        return redirect('baseApp:solicitudes')

    context = {'form':form}
    return render(request, 'base/solicitud_create.html', context)


def DetailsSolicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
        
    context = { 'solicitud':solicitud }
    return render(request, 'base/solicitud_details.html', context)


def UpdateSolicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    form = SolicitudUpdateForm(request.POST or None, instance=solicitud)

    if request.method == 'POST':
        if form.is_valid():
            updated_solicitud = form.save()           

        return redirect('baseApp:detalles_solicitud', solicitud_pk=solicitud.pk)
    
    elif request.method == 'GET':
        context = {'form':form}
        return render(request, 'base/solicitud_update.html', context)


def DeleteSolicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('baseApp:solicitudes')

    context = {'solicitud': solicitud}
    return render(request, 'base/solicitud_delete.html', context)


def generate_PDF_document(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    ct = datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")    

    context = { 'solicitud':solicitud, 'current_time':ct }

    pdf = render_to_pdf('base/pdf_document.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Ficha técnica solicitud de sustracción'
        content = f'attachment; filename="{filename}.pdf"'
        response['Content-Disposition'] = content
        return response
    return HttpResponse('Error: Not found')