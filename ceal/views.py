from django.shortcuts import render

# Create your views here.
def ceal_index(request):
    return render(request, 'ceal/index.html')
