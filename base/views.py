from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudCreateForm, SolicitudUpdateForm
from .utils import *
import datetime
# from django.contrib.auth.decorators import login_required
from .decorators import user_is_solicitud_author, login_required


@login_required
def ListSolicitudes(request):
    solicitudes = Solicitud.objects.all().order_by('-created_at')
    context = { 'solicitudes':solicitudes}
    return render(request, 'base/solicitud_list.html', context)

@login_required
def CreateSolicitud(request):
    form = SolicitudCreateForm(request.POST or None)
    if form.is_valid():
        nueva_solicitud = form.save(commit=False)
        nueva_solicitud.autor = request.user
        nueva_solicitud.save()
       
        return redirect('baseApp:solicitudes')

    context = {'form':form}
    return render(request, 'base/solicitud_create.html', context)

@login_required
def DetailsSolicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
        
    context = { 'solicitud':solicitud }
    return render(request, 'base/solicitud_details.html', context)


@user_is_solicitud_author
def UpdateSolicitud(request, solicitud_pk):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_pk)
    form = SolicitudUpdateForm(request.POST or None, instance=solicitud)

    if request.method == 'POST':
        if form.is_valid():
            updated_solicitud = form.save()           

        return redirect('baseApp:detalles_solicitud', solicitud_pk=solicitud.pk)
    
    elif request.method == 'GET':
        context = {
            'form':form,
            'solicitud_pk':solicitud_pk
        }
        return render(request, 'base/solicitud_update.html', context)


@user_is_solicitud_author
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


# TODO:

# transferencia de "propiedad" de solicitudes
# configurar variables de entornos
# configurar correo SMTP
# carga de documentos?