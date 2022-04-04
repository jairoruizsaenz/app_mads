from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudCreateForm


def Home(request):
    context = { 'mensaje': 'Este es un mensaje de prueba' }    
    return render(request, 'base/inicio.html', context)


# def ListSolicitudes(request):
#     solicitudes = Solicitud.objects.all().order_by('-created_at')
#     context = { 'solicitudes':solicitudes }
#     return render(request, 'base/solicitudes_list.html', context)


def CreateMapa(request):
    form = SolicitudCreateForm(request.POST or None)
    if form.is_valid():
        solicitud_nueva = form.save()
        # return redirect('baseApp:lista-mapas')

    context = {'form':form}
    return render(request, 'base/solicitud_create.html', context)