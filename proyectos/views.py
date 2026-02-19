from django.shortcuts import render

# Create your views here.
def proyectos_index(request):
    return render(request, 'proyectos/index.html')