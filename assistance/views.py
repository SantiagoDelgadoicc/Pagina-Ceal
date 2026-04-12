from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Ayudantia, Tutoria, SolicitudAcademica

def assistance_index(request: HttpRequest):
    return render(request, 'assistance/index.html', {
        'ayudantias': Ayudantia.objects.all(),
        'tutorias': Tutoria.objects.all(),
        'solicitudes': SolicitudAcademica.objects.filter(is_approved=True)
    })

def crear_solicitud(request: HttpRequest):
    if request.method == 'POST':
        ramo = request.POST.get('ramo')
        cantidad = request.POST.get('cantidad')
        contacto = request.POST.get('info_contacto')
        fecha = request.POST.get('fecha_limite')

        if ramo and fecha and contacto:
            SolicitudAcademica.objects.create(
                ramo=ramo,
                cantidad_estudiantes=cantidad,
                info_contacto=contacto,
                fecha_limite=fecha
            )
        return redirect('assistance_index')
    
    return redirect('assistance_index')