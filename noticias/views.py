from django.shortcuts import render

# Create your views here.
def noticias_index(request):
    return render(request, 'noticias/index.html')