from django.shortcuts import render

# Create your views here.
def news_index(request):
    return render(request, 'news/index.html')

from django.shortcuts import render
from .models import News

def index(request):
    noticias = News.objects.all() 
    print(f"DEBUG: Tienes {noticias.count()} noticias en la base de datos")
    return render(request, 'news/index.html', {'noticias': noticias})