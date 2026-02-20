from django.shortcuts import render

# Create your views here.
def computing_index(request):
    return render(request, 'computing/index.html')