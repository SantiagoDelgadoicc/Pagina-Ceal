from django.shortcuts import render

# Create your views here.
def calendario_index(request):
    return render(request, 'calendario/index.html')