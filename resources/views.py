from django.shortcuts import render
from .models import AcademicResource

def resources_index(request):
    resource = AcademicResource.objects.first()
    return render(request, 'resources/index.html', {'resource': resource})