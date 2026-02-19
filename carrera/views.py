from django.shortcuts import render

# Create your views here.
def carrera_index(request):
    return render(request, 'carrera/index.html')