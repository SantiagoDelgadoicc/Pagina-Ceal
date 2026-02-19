from django.shortcuts import render

# Create your views here.
def ayudas_index(request):
    return render(request, 'ayudas/index.html')